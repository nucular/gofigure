import datetime

import gofigure.parsers

class EnergyMechParser(gofigure.parsers.Parser):
    """
    Implements support for EnergyMech-style logs.
    These are always stored under file names like %s_%c_%Y%m%d.log and keep the
    time in the lines so looking them up is trivial though we still have to
    search for our start and end lines.
    """

    def __init__(self, root, channel="", server="", filenames="%s_%c_%Y%m%d.log"):
        """
        Initializes the Parser.
        root: the root directory of your logs
        channel: the channel to find logs for
        server: the server the client is connected to when the logs are written
        filenames: the filename format of the log files, usually
            "%s_%c_%Y%m%d.log" (in strftime format, %s replaced with the server,
            %c with the channel)
        """
        self.root = root
        self.channel = channel
        self.network = network
        self.filenames = filenames.replace("%s", server).replace("%c", channel)

    def parseTime(self, line):
        """Parse only the time of a line from a log file into a time instance."""
        timestr = line.split(" ", 1)[0][1:-1]
        if len(timestr) == 8:
            return datetime.time.strptime(timestr, "%H:%M:%S")
        elif len(timestr) == 5:
            return datetime.time.strptime(timestr, "%H:%M")
        else:
            raise ValueError("Unknown time format: '{}'".format(timestr))

    def parse(self, line):
        """Parse a line from a log file into an Event instance."""
        splittype = line.split(" ", 2)
        splitspace = line.split(" ")
        time = self.parseTime(line)

        # *** Meta
        if splittype[0] == "***":
            return
        # [time] <nick> message
        elif splittype[1][0] == "<":
            nick, message = splittype[1][1:-1], splittype[2][:-1]
            return gofigure.events.MessageEvent(time, nick, message)
        # [time] * nick message
        elif splittype[1] == "*":
            splitme = line.split(" ", 3)
            nick, message = splitme[2], splitme[3][:-1]
            return gofigure.events.ActionEvent(time, nick, message)
        # [time] -nick- message
        elif splittype[1][0] == "-" and splittype[1][-1] == "-":
            nick, message = splittype[1][1:-1], splittype[2][:-1]
            return gofigure.events.NoticeEvent(time, nick, message)
        # [time] Joins: nick (host)
        elif splitspace[2] == "Joins:":
            nick, host = splitspace[3], splitspace[4][1:-2]
            return gofigure.events.JoinEvent(time, nick, host)
        # [time] Parts: nick (host) (message)
        elif splitspace[2] == "Parts:":
            splitpart = line.split(" ", 5)[3:]
            nick, host, reason = splitpart[0], splitpart[1][1:-1], splitpart[2][1:-2]
            return gofigure.events.PartEvent(time, nick, host, reason)
        # [time] Quits: nick (host) (message)
        elif splitspace[2] == "Quits:"
            splitquit = line.split(" ", 5)[3:]
            nick, host, reason = splitquit[0], splitquit[1][1:-1], splitquit[2][1:-2]
            return gofigure.events.QuitEvent(time, nick, host, reason)
        # [time] kickee was kicked by nick (reason)
        elif " ".join(splitspace[3:5]) == "was kicked":
            kicked, nick, reason = splitspace[2], splitspace[6], splitspace[7][1:-2]
            return gofigure.events.KickEvent(time, nick, kicked, reason)
        # [time] nick is now known as newnick
        elif " ".join(splitspace[3:7]) == "is now known as":
            nick, newnick = splitspace[2], splitspace[-1][:-1]
            return gofigure.events.NickEvent(time, nick, newnick)
        # [time] nick sets mode mode
        elif " ".join(splitspace[3:5]) == "sets mode:":
            splitmode = line.split(" ", 5)
            nick, mode = splitmode[2], splitmode[5][:-1]
            return gofigure.events.ModeEvent(time, nick, mode)
        elif " ".join(space_parse[3:5]) == "changes topic":
            nick, topic = splitspace[2], line.split(" ", 6)[6]
            return gofigure.events.TopicEvent(time, nick, topic)

    def __getitem__(self, key):
        """
        Returns a generator of all IRC events between two datetime instances
        passed using slicing.
        """
        date = datetime.date(key.start.year, key.start.month, key.start.day,
            tzinfo=key.start.tzinfo)
        while date <= key.end.date:
            filename = datetime.strftime(date, self.filenames)
            with open(filename, "rt") as f:
                for line in f.readlines():
                    time = self.parseTime(line).replace(tzinfo=date.tzinfo)
                    if (date > key.start.date and date < key.end.date)
                        or (date == key.start.date and time >= key.start.time)
                        or (date == key.end.date and time <= key.end.time):
                        yield self.parse(line)
            date += datetime.timedelta(day=1)
