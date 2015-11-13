from abc import ABCMeta

class Figure(object):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        raise NotImplementedError()
