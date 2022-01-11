from Trump import *


class Distribution(Trump):
    def __init__(self):
        super().__init__()
        self.nb_players = 4
        #self.number_order = [i for i in range(4)]
        self.min_range_give_cards = 0
        self.max_range_give_cards = 3
        self.give_cards = 3
        self.give_cards_turn = 1
        self.trump_card = None
        self.trump_card_nb = 0
        self.play = Player.players(self)
        self.second_dist = False
        #deck mélangé
        #self.player_number = [Player.players(self) for i in range(self.nb_players)]

    def update_dist(self):
        self.shuffle_deck = Shuffle.shuffle(self)
        self.card_distribution()
        self.new_trump()
        self.min_range_give_cards = 0
        self.max_range_give_cards = 3
        self.give_cards_turn = 1
        for i in range(self.nb_players):
            self.player_number = [Player.players(self) for i in range(self.nb_players)]
        print(f"new_trump_color : {self.new_trump_color}")
        if self.new_trump_color is not None:
            self.second_dist = True
            self.card_distribution()
            self.min_range_give_cards = 0
            self.max_range_give_cards = 3
            self.trump_card_nb = 0
            self.give_cards_turn = 1

    def card_distribution(self):
        while self.give_cards_turn <= 2:
            for i in range(self.nb_players):
                for j in range(self.min_range_give_cards, self.max_range_give_cards):
                    self.player_number[i].append(self.shuffle_deck[j])
                if self.give_cards_turn == 1 and i != self.nb_players - 1:
                    self.min_range_give_cards += 3
                    self.max_range_give_cards += 3
                elif self.give_cards_turn == 2 and i != self.nb_players - 1:
                    self.min_range_give_cards += 2
                    self.max_range_give_cards += 2
            if self.give_cards_turn < 2:
                self.min_range_give_cards += 3
                self.max_range_give_cards += 2
            self.give_cards_turn += 1
            if not self.second_dist:
                print(f"{self.azimuth[self.number_order[0]]} : {self.player_number[0]}")
        if self.second_dist:
            self.min_range_give_cards += 3
            self.max_range_give_cards += 4
            #print(f"trump_player = {self.trump_player}")
            for i in range(self.nb_players):
                if i == self.trump_player:
                    self.player_number[i].append(self.shuffle_deck[self.trump_card_nb])
                    self.max_range_give_cards -= 1
                for j in range(self.min_range_give_cards, self.max_range_give_cards):
                    self.player_number[i].append(self.shuffle_deck[j])
                if i == self.trump_player:
                    self.min_range_give_cards += 2
                    self.max_range_give_cards += 3
                else:
                    self.min_range_give_cards += 3
                    self.max_range_give_cards += 3
        """            
        for i in range(self.nb_players):
            print(f"{self.azimuth[self.number_order[i]]} : {self.player_number[i]}")
        """
        return self.player_number

    def draw_trump_card(self):
        self.trump_card = self.shuffle_deck[self.min_range_give_cards + 2]
        self.trump_card_nb = self.min_range_give_cards + 2
        print(f"self.trump_card : {self.trump_card}")
        return self.trump_card

    def new_trump(self):
        return Trump.trump_color(self, self.draw_trump_card())
