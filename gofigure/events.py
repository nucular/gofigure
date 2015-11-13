import abc

class Event(object):
    """Encapsulates an IRC event."""
    __metaclass__ = abc.ABCMeta

class MessageEvent(Event):
    """A PRIVMSG event."""
    command = "PRIVMSG"
    def __init__(self, time, nick, message):
        self.time = time
        self.nick = nick
        self.message = message

class ActionEvent(Event):
    """A PRIVMSG action event."""
    command = "PRIVMSG"
    def __init__(self, time, nick, message):
        self.time = time
        self.nick = nick
        self.message = message

class NoticeEvent(Event):
    """A NOTICE event."""
    command = "NOTICE"
    def __init__(self, time, nick, message):
        self.time = time
        self.nick = nick
        self.message = message

class JoinEvent(Event):
    """A JOIN event."""
    command = "JOIN"
    def __init__(self, time, nick):
        self.time = time
        self.nick = nick

class PartEvent(Event):
    """A PART event."""
    command = "PART"
    def __init__(self, time, nick, reason):
        self.time = time
        self.nick = nick
        self.reason = reason

class QuitEvent(Event):
    """A QUIT event."""
    command = "QUIT"
    def __init__(self, time, nick, reason):
        self.time = time
        self.nick = nick
        self.reason = reason

class KickEvent(Event):
    """A KICK event."""
    command = "KICK"
    def __init__(self, time, nick, kicked, reason):
        self.time = time
        self.nick = nick
        self.kicked = kicked
        self.reason = reason

class NickEvent(Event):
    """A NICK event."""
    command = "NICK"
    def __init__(self, time, nick, newnick):
        self.time = time
        self.nick = nick
        self.newnick = newnick

class ModeEvent(Event):
    """A MODE event."""
    command = "MODE"
    def __init__(self, time, nick, mode):
        self.time = time
        self.nick = nick
        self.mode = mode

class TopicEvent(Event):
    """A TOPIC event."""
    command = "TOPIC"
    def __init__(self, time, nick, topic):
        self.time = time
        self.nick = nick
        self.topic = topic
