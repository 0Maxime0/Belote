from Game import *


class Belote(Game):
    def __init__(self):
        super().__init__()

    def start_game(self):
        while self.NS_total < 500 or self.EW_total < 500:
            Game.playing(self)
            if self.new_trump_color is not None:
                Game.new_game(self)
            else:
                self.shuffle_deck = Shuffle.shuffle(self)
                Game.reinitialisation(self)
                Game.playing(self)
        if self.NS_total > self.EW_total:
            print("North et South vainqueurs ")
        if self.EW_total > self.NS_total:
            print("East et West vainqueurs")

game = Belote()
game.start_game()






