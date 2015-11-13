from abc import ABCMeta

class Parser(object):
    """
    Implements the immutable sequence protocol.
    Abstract base class for subclasses that read in IRC logs from various file
    formats and directory structures and convert them to a list of sequences.
    """
    __metaclass__ = ABCMeta

    def __getitem__(self, key):
        """
        Returns a list of all IRC events between two datetime instances passed
        using slicing. This is an expensive operation since it often involves
        binary searching of multiple files.
        """
        pass

    def __len__(self):
        """
        The actual length of the IRC logs is hard to determine without opening
        and scanning all files, so we assume infinite length.
        """
        return float("inf")
