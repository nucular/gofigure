import abc

class Parser(object):
    """
    Implements the immutable sequence protocol.
    Abstract base class for subclasses that read in IRC logs from various file
    formats and directory structures and convert them to a list of sequences.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, root):
        """
        Initializes the Parser.
        root: the root directory of your logs
        """
        pass

    def __getitem__(self, key):
        """
        Returns a generator of all IRC events between two datetime instances
        passed using slicing. This is an expensive operation since it often
        involves searching multiple files for time stamps.
        """
        pass

    def __len__(self):
        """
        The actual length of the IRC logs is hard to determine without opening
        and scanning all files, so we assume infinite length.
        """
        return float("inf")
