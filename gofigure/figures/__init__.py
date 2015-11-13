import abc

class Figure(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        raise NotImplementedError()
