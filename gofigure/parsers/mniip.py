import os.path
import datetime

import gofigure.parsers
import gofigure.events

class MniipParser(gofigure.parsers.Parser):
    """
    Implements support for mniip's logs for testing purposes.
    These are always stored under file names like %Y-%m-%d.txt and keep the
    time in the lines so looking them up is trivial though we still have to
    search for our start and end lines.
    """

    def __init__(self, root, channel, server, filenames="%Y-%m-%d.txt"):
        """
        Initializes the Parser.
        root: the root directory of your logs
        channel: the channel to find logs for
        server: the server the client is connected to when the logs are written
        filenames: the filename format of the log files, usually
            "%Y-%m-%d.txt" (in strftime format)
        """
        self.root = root
        self.channel = channel
        self.server = server
        self.filenames = filenames

    def parseTime(self, line):
        """Parse only the time of a line from a log file into a time instance."""
        timestr = line.split(" ", 1)[0][1:-1]
        if len(timestr) == 8:
            return datetime.datetime.strptime(timestr, "%H:%M:%S").time()
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
        # [time] *** nick has joined channel
        elif splitspace[2] == "***" and " ".join(splitspace[4:6] == "has joined":
            nick = splitspace[3]
            return gofigure.events.JoinEvent(time, nick, "")
        # [time] *** nick has parted channel (message)
        elif splitspace[2] == "***" and splitspace[3:4] == "has parted":
            splitpart = line.split(" ", 7)[3:]
            nick, reason = splitpart[0], splitpart[4][1:-2]
            return gofigure.events.PartEvent(time, nick, "", reason)
        # [time] *** nick has quit (message)
        elif splitspace[2] == "***" and " ".join(splitspace[4:6] == "has quit":
            splitquit = line.split(" ", 5)[2:]
            nick, reason = splitquit[0], splitquit[3][1:-2]
            return gofigure.events.QuitEvent(time, nick, "", reason)
        # [time] *** kickee was kicked by nick from channel (reason)
        elif splitspace[2] = "***" and " ".join(splitspace[4:6]) == "was kicked by":
            kicked, nick, reason = splitspace[3], splitspace[7], splitspace[10][1:-2]
            return gofigure.events.KickEvent(time, nick, kicked, reason)
        # [time] *** nick has changed nick to newnick
        elif splitspace[2] = "***" and " ".join(splitspace[4:8]) == "has changed nick to":
            nick, newnick = splitspace[3], splitspace[-1]
            return gofigure.events.NickEvent(time, nick, newnick)
        # [time] *** nick set mode mode
        elif splitspace[2] = "***" and " ".join(splitspace[4:6]) == "set mode":
            splitmode = line.split(" ", 6)
            nick, mode = splitmode[3], splitmode[6]
            return gofigure.events.ModeEvent(time, nick, mode)
        # [time] *** nick has changed topic of channel to: topic
        elif splitspace[2] = "***" and " ".join(space_parse[4:8]) == "has changed topic of":
            nick, topic = splitspace[3], line.split(" ", 10)[10]
            return gofigure.events.TopicEvent(time, nick, topic)

    def __getitem__(self, key):
        """
        Returns a generator of all IRC events between two datetime instances
        passed using slicing.
        """
        date = datetime.date(key.start.year, key.start.month, key.start.day)
        startdate = key.start.date()
        starttime = key.start.time()
        stopdate = key.stop.date()
        stoptime = key.stop.time()
        while date <= stopdate:
            filename = datetime.datetime.strftime(date, self.filenames)
            try:
                with open(os.path.join(self.root, filename), "rt") as f:
                    for line in f.readlines():
                        time = self.parseTime(line).replace(tzinfo=key.start.tzinfo)
                        if (date > startdate and date < stopdate) \
                            or (date == startdate and time >= starttime) \
                            or (date == stopdate and time <= stoptime):
                            yield self.parse(line)
            except IOError:
                pass
            finally:
                date += datetime.timedelta(days=1)
