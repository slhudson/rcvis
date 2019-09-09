from .colors import Color

class Item:
    def __init__(self, name, color):
        assert(isinstance(color, Color))
        self.name = name
        self.color = color

class Transfer:
    def __init__(self, item, transfers):
        """ Transfers is a mapping from Item objects
            to a number of transferred votes. """
        self.item = item
        self.transfers = transfers
class Elimination(Transfer): pass
class WinTransfer(Transfer): pass

class Step:
    def __init__(self):
        self.winners = []
        self.transfers = []