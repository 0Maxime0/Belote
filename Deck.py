from Color import *


class Deck(Color):
    def __init__(self):
        super().__init__()
        self.deck = []

    def classic_deck(self):
        self.deck = Color.spade(self) + Color.clover(self) + Color.heart(self) + Color.diamond(self)
        #print(self.deck)
        return self.deck


"""a = Deck()
a.classic_deck()"""
