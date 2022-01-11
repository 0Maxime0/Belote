from Card import *


class Color(Card):
    def __init__(self):
        super().__init__()
        self.spade_color = {}
        self.clover_color = {}
        self.heart_color = {}
        self.diamond_color = {}
        self.spade_name = "spade"
        self.clover_name = "clover"
        self.heart_name = "heart"
        self.diamond_name = "diamond"

    def spade(self):
        self.spade_color = [{(Card.card_nam(self)[i], self.spade_name): Card.card_value(self)[i]} for i in range(len(Card.card_nam(self)))]
        return self.spade_color

    def clover(self):
        self.clover_color = [{(Card.card_nam(self)[i], self.clover_name): Card.card_value(self)[i]} for i in range(len(Card.card_nam(self)))]
        return self.clover_color

    def heart(self):
        self.heart_color = [{(Card.card_nam(self)[i], self.heart_name): Card.card_value(self)[i]} for i in range(len(Card.card_nam(self)))]
        return self.heart_color

    def diamond(self):
        self.diamond_color = [{(Card.card_nam(self)[i], self.diamond_name): Card.card_value(self)[i]} for i in range(len(Card.card_nam(self)))]
        return self.diamond_color


"""
c = Color()
print(c.spade())
print(c.clover())
print(c.heart())
print(c.diamond())
"""