from Shuffle import *
from Player import *


class Trump(Shuffle, Player):
    def __init__(self):
        super().__init__()
        self.trump = None
        self.actual_trump_color = None
        self.new_trump_color = None
        self.new_val = 0
        self.new_val_deck = 0
        self.choice = ''
        self.Y_choice = False
        self.trump_player = 0
        self.nine_pos = None
        self.jack_pos = None
        self.trump_test = 0
        self.spade_test = 0
        self.clover_test = 0
        self.heart_test = 0
        self.diamond_test = 0
        self.all_test = None
        self.player_number = [Player.players(self) for i in range(4)]
        self.number_order = [i for i in range(4)]
        self.azimuth = {0: "North", 1: "East", 2: "South", 3: "West"}

    def trump_color(self, trump_card):
        self.trump = trump_card
        self.actual_trump_color = list(trump_card.keys())[0][1]
        #self.new_trump_color = self.trump[0][1]
        print(f"actual trump color : {self.actual_trump_color}")
        self.choose_trump()
        if self.new_trump_color is not None:
            self.J_nine_value()

    def choose_trump(self):
        #condition si les deux tours se finisse sur non
        #exception lors de l'input par lutilisateur
        print(f"trump : {self.trump}")
        for i in range(4):
            if self.azimuth[self.number_order[i]] == "North":
                self.choice = input(f"Voulez vous cette carte comme atout : {self.actual_trump_color}(Y/N) :")
                if self.choice == 'Y':
                    print("OUI")
                    self.new_trump_color = self.actual_trump_color
                    return self.new_trump_color
                if self.choice == 'N':
                    print("UNE")
                    self.trump_player += 1
            else:
                if list(self.trump.keys())[0][0] == '7' or list(self.trump.keys())[0][0] == '8' or list(self.trump.keys())[0][0] == 'Q':
                    self.trump_test += 1
                elif list(self.trump.keys())[0][0] == 'K' or list(self.trump.keys())[0][0] == '10':
                    self.trump_test += 3
                elif list(self.trump.keys())[0][0] == 'As':
                    self.trump_test += 4
                elif list(self.trump.keys())[0][0] == '9':
                    self.trump_test += 5
                else:
                    self.trump_test += 7
                #print(self.trump_test)
                for j in range(len(self.player_number[i])):
                    if list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and (list(self.player_number[i][j].keys())[0][0] == '7' or list(self.player_number[i][j].keys())[0][0] == '8' or list(self.player_number[i][j].keys())[0][0] == 'Q'):
                        self.trump_test += 1
                    elif list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and (list(self.player_number[i][j].keys())[0][0] == 'K' or list(self.player_number[i][j].keys())[0][0] == '10'):
                        self.trump_test += 3
                    elif list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'As':
                        self.trump_test += 4
                    elif list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == '9':
                        self.trump_test += 5
                    elif list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'J':
                        self.trump_test += 7
                    elif list(self.player_number[i][j].keys())[0][1] != self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'As':
                        self.trump_test += 1
                #print(self.trump_test)
                if self.trump_test >= 10:
                    self.new_trump_color = self.actual_trump_color
                    #print(self.player_number[i])
                    return self.new_trump_color
                else:
                    print("UNE")
                    self.trump_player += 1
                    self.trump_test = 0
                    #print(self.trump_test)
        self.trump_player = 0
        for i in range(4):
            if self.azimuth[self.number_order[i]] == "North":
                self.choice = input(f"Voulez vous choisir une couleur d'atout? (Y/N) : ")
                if self.choice == 'Y':
                    print("OUI")
                    self.new_trump_color = self.new_trump_color
                    while self.actual_trump_color == self.new_trump_color:
                        self.new_trump_color = input(f"Choisissez une couleur d'atout : ")
                        if self.actual_trump_color == self.new_trump_color:
                            print("Vous ne pouvez pas sélectionner la même couleur que la carte")
                    if self.new_trump_color == "spade":
                        print("Atout pique")
                        return self.new_trump_color
                    elif self.new_trump_color == "clover":
                        print("Atout trèfle")
                        return self.new_trump_color
                    elif self.new_trump_color == "heart":
                        print("Atout coeur")
                        return self.new_trump_color
                    elif self.new_trump_color == "diamond":
                        print("Atout carreau")
                        return self.new_trump_color
                if self.choice == 'N':
                    print("DEUX")
                    self.trump_player += 1
            else:
                self.trump_test = 0
                self.spade_test = 0
                self.clover_test = 0
                self.heart_test = 0
                self.diamond_test = 0
                if list(self.trump.keys())[0][0] == 'As':
                    if self.actual_trump_color == "spade":
                        self.clover_test += 1
                        self.heart_test += 1
                        self.diamond_test += 1
                    elif self.actual_trump_color == "clover":
                        self.spade_test += 1
                        self.heart_test += 1
                        self.diamond_test += 1
                    elif self.actual_trump_color == "heart":
                        self.spade_test += 1
                        self.clover_test += 1
                        self.diamond_test += 1
                    elif self.actual_trump_color == "diamond":
                        self.spade_test += 1
                        self.clover_test += 1
                        self.heart_test += 1
                for j in range(len(self.player_number[i])):
                    if list(self.player_number[i][j].keys())[0][1] == "spade" and self.actual_trump_color != "spade" and (list(self.player_number[i][j].keys())[0][0] == '7' or list(self.player_number[i][j].keys())[0][0] == '8' or list(self.player_number[i][j].keys())[0][0] == 'Q'):
                        self.spade_test += 1
                    elif list(self.player_number[i][j].keys())[0][1] == "spade" and self.actual_trump_color != "spade" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and (list(self.player_number[i][j].keys())[0][0] == 'K' or list(self.player_number[i][j].keys())[0][0] == '10'):
                        self.spade_test += 3
                    elif list(self.player_number[i][j].keys())[0][1] == "spade" and self.actual_trump_color != "spade" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'As':
                        self.spade_test += 4
                    elif list(self.player_number[i][j].keys())[0][1] == "spade" and self.actual_trump_color != "spade" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == '9':
                        self.spade_test += 5
                    elif list(self.player_number[i][j].keys())[0][1] == "spade" and self.actual_trump_color != "spade" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'J':
                        self.spade_test += 7
                    elif list(self.player_number[i][j].keys())[0][1] == "clover" and self.actual_trump_color != "clover" and (list(self.player_number[i][j].keys())[0][0] == '7' or list(self.player_number[i][j].keys())[0][0] == '8' or list(self.player_number[i][j].keys())[0][0] == 'Q'):
                        self.clover_test += 1
                    elif list(self.player_number[i][j].keys())[0][1] == "clover" and self.actual_trump_color != "clover" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and (list(self.player_number[i][j].keys())[0][0] == 'K' or list(self.player_number[i][j].keys())[0][0] == '10'):
                        self.clover_test += 3
                    elif list(self.player_number[i][j].keys())[0][1] == "clover" and self.actual_trump_color != "clover" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'As':
                        self.clover_test += 4
                    elif list(self.player_number[i][j].keys())[0][1] == "clover" and self.actual_trump_color != "clover" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == '9':
                        self.clover_test += 5
                    elif list(self.player_number[i][j].keys())[0][1] == "clover" and self.actual_trump_color != "clover" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'J':
                        self.clover_test += 7
                    elif list(self.player_number[i][j].keys())[0][1] == "heart" and self.actual_trump_color != "heart" and (list(self.player_number[i][j].keys())[0][0] == '7' or list(self.player_number[i][j].keys())[0][0] == '8' or list(self.player_number[i][j].keys())[0][0] == 'Q'):
                        self.heart_test += 1
                    elif list(self.player_number[i][j].keys())[0][1] == "heart" and self.actual_trump_color != "heart" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and (list(self.player_number[i][j].keys())[0][0] == 'K' or list(self.player_number[i][j].keys())[0][0] == '10'):
                        self.heart_test += 3
                    elif list(self.player_number[i][j].keys())[0][1] == "heart" and self.actual_trump_color != "heart" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'As':
                        self.heart_test += 4
                    elif list(self.player_number[i][j].keys())[0][1] == "heart" and self.actual_trump_color != "heart" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == '9':
                        self.heart_test += 5
                    elif list(self.player_number[i][j].keys())[0][1] == "heart" and self.actual_trump_color != "heart" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'J':
                        self.heart_test += 7
                    elif list(self.player_number[i][j].keys())[0][1] == "diamond" and self.actual_trump_color != "diamond" and (list(self.player_number[i][j].keys())[0][0] == '7' or list(self.player_number[i][j].keys())[0][0] == '8' or list(self.player_number[i][j].keys())[0][0] == 'Q'):
                        self.diamond_test += 1
                    elif list(self.player_number[i][j].keys())[0][1] == "diamond" and self.actual_trump_color != "diamond" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and (list(self.player_number[i][j].keys())[0][0] == 'K' or list(self.player_number[i][j].keys())[0][0] == '10'):
                        self.diamond_test += 3
                    elif list(self.player_number[i][j].keys())[0][1] == "diamond" and self.actual_trump_color != "diamond" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'As':
                        self.diamond_test += 4
                    elif list(self.player_number[i][j].keys())[0][1] == "diamond" and self.actual_trump_color != "diamond" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == '9':
                        self.diamond_test += 5
                    elif list(self.player_number[i][j].keys())[0][1] == "diamond" and self.actual_trump_color != "diamond" and list(self.player_number[i][j].keys())[0][1] == self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'J':
                        self.diamond_test += 7
                    elif list(self.player_number[i][j].keys())[0][1] != self.actual_trump_color and list(self.player_number[i][j].keys())[0][0] == 'As':
                        self.spade_test += 1
                        self.clover_test += 1
                        self.heart_test += 1
                        self.diamond_test += 1
                if self.actual_trump_color == "spade":
                    self.all_test = [{self.clover_test: "clover"}, {self.heart_test: "heart"}, {self.diamond_test: "diamond"}]
                    self.trump_test = list(self.all_test[0].keys())[0]
                    for j in range(1, len(self.all_test)):
                        print(list(self.all_test[j].keys()))
                        if self.trump_test < list(self.all_test[j].keys())[0]:
                            self.trump_test = list(self.all_test[j].keys())[0]
                        if self.trump_test >= 10:
                            self.new_trump_color = self.all_test[self.trump_test]
                            return self.new_trump_color
                elif self.actual_trump_color == "clover":
                    self.all_test = [{self.spade_test: "spade"}, {self.heart_test: "heart"}, {self.diamond_test: "diamond"}]
                    self.trump_test = list(self.all_test[0].keys())[0]
                    for j in range(1, len(self.all_test)):
                        print(list(self.all_test[j].keys()))
                        if self.trump_test < list(self.all_test[j].keys())[0]:
                            self.trump_test = list(self.all_test[j].keys())[0]
                        if self.trump_test >= 10:
                            self.new_trump_color = self.all_test[self.trump_test]
                            return self.new_trump_color
                elif self.actual_trump_color == "heart":
                    self.all_test = [{self.spade_test: "spade"}, {self.clover_test: "clover"}, {self.diamond_test: "diamond"}]
                    self.trump_test = list(self.all_test[0].keys())[0]
                    for j in range(1, len(self.all_test)):
                        print(list(self.all_test[j].keys()))
                        if self.trump_test < list(self.all_test[j].keys())[0]:
                            self.trump_test = list(self.all_test[j].keys())[0]
                        if self.trump_test >= 10:
                            self.new_trump_color = self.all_test[self.trump_test]
                            return self.new_trump_color
                elif self.actual_trump_color == "diamond":
                    self.all_test = [{self.spade_test: "spade"}, {self.clover_test: "clover"}, {self.heart_test: "heart"}]
                    self.trump_test = list(self.all_test[0].keys())[0]
                    for j in range(1, len(self.all_test)):
                        if self.trump_test < list(self.all_test[j].keys())[0]:
                            self.trump_test = list(self.all_test[j].keys())[0]
                        if self.trump_test >= 10:
                            self.new_trump_color = self.all_test[self.trump_test]
                            return self.new_trump_color
                else:
                    print("DEUX")




        return self.new_trump_color

    def J_nine_value(self):
        #changer la valeur des cartes de l'atout
        #9
        self.nine_pos = self.shuffle_deck.index({('9', self.new_trump_color): 0})
        #print(self.nine_pos)
        #print(self.shuffle_deck[self.nine_pos])
        self.shuffle_deck[self.nine_pos][('9', self.new_trump_color)] = 14
        #print(list(self.shuffle_deck[self.nine_pos].values()))
        #jack
        self.jack_pos = self.shuffle_deck.index({('J', self.new_trump_color): 2})
        #print(self.jack_pos)
        #print(self.shuffle_deck[self.jack_pos])
        self.shuffle_deck[self.jack_pos][('J', self.new_trump_color)] = 20
        #print(list(self.shuffle_deck[self.jack_pos].values()))
        #print(self.shuffle_deck)

