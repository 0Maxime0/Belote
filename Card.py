

class Card:
    def __init__(self):
        self.card_val = 0
        self.color_set = []
        self.card_name = ""
        self.all_val = 0
        self.all_name = ""

    def seven(self, card_val):
        self.card_name = "7"
        return card_val, self.card_name

    def eight(self, card_val):
        self.card_name = "8"
        return card_val, self.card_name

    def nine(self, card_val):
        self.card_name = "9"
        return card_val, self.card_name

    def ten(self, card_val):
        self.card_name = "10"
        return card_val, self.card_name

    def jack(self, card_val):
        self.card_name = "J"
        return card_val, self.card_name

    def queen(self, card_val):
        self.card_name = "Q"
        return card_val, self.card_name

    def king(self, card_val):
        self.card_name = "K"
        return card_val, self.card_name

    def one(self, card_val):
        self.card_name = "As"
        return card_val, self.card_name

    def card_nam(self):
        self.all_name = [self.seven(0)[1], self.eight(0)[1], self.nine(0)[1], self.ten(10)[1],
                         self.jack(2)[1], self.queen(3)[1], self.king(4)[1], self.one(11)[1]]
        return self.all_name

    def card_value(self):
        self.all_val = [self.seven(0)[0], self.eight(0)[0], self.nine(0)[0], self.ten(10)[0],
                        self.jack(2)[0], self.queen(3)[0], self.king(4)[0], self.one(11)[0]]
        return self.all_val

