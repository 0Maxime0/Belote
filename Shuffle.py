from Deck import *
import random


class Shuffle(Deck):
    def __init__(self):
        super().__init__()
        self.shuffle_deck = None

    def shuffle(self):
        self.shuffle_deck = Deck.classic_deck(self)
        random.shuffle(self.shuffle_deck)
        #print(f"shuffle deck : {self.shuffle_deck}")
        return self.shuffle_deck


"""rc = Shuffle()
rc.shuffle()"""

