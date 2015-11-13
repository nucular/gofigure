import os.path
import glob

import gofigure.parsers

class XChatParser(gofigure.parsers.Parser):
    """
    Implements support for XChat and HexChat-style logs.
    This is done by first glob-matching and scanning the dates from all files
    that might be logs according to the name format, then searching the first
    and last file that fall inside the requested date splice for the start and
    end lines.
    """

    def __init__(self, root, channel="", network="", server="",
        filenames="%c.log", timestamp="%b %d %H:%M:%S "):
        """
        Initializes the Parser and searches for all possible log files.
        root: the root directory of your logs, usually ~/.xchat2/xchatlogs for
            XChat and /.config/hexchat/logs for HexChat (can be relative too)
        channel: the channel to find logs for (has no effect if %c isn't used
            in filenames)
        network: the IRC network the channel resides in (has no effect if %n
            isn't used in filenames)
        server: the server the client is connected to when the logs are written
            (has no effect if %s isn't used in filenames)
        filenames: whatever you have entered in the "Log filename" text box
            under Preferences > Logging
        timestamp: whatever you have entered in the "Log timestamp format" text
            box under Preferences > Logging
        """
        self.filenames = glob.glob(os.path.join(
            root,
            filenames
                .replace("%c", channel)
                .replace("%n", network)
                .replace("%s", server)
        ), recursive=False)
        self.timestamp = timestamp

        raise NotImplementedError()
