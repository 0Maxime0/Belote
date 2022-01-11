from Draw import *


class Game(Distribution):
    def __init__(self):
        super().__init__()
        self.choose_card = 0
        self.play_card = None
        self.actual_turn = []
        self.most_powerful_card = None
        self.play_color = None
        self.trump_possession = False
        self.first_player = 0
        self.first_player_position = 0
        self.next_number_order = []
        self.next_player = 0
        self.next_player_position = 0
        self.next_order = []
        self.trump_on_the_board = False
        self.highest_trump = None
        self.test = False
        self.play_ok = False
        self.fold = []
        self.fold_winner = None
        self.NS_fold = []
        self. EW_fold = []
        self.NS_score = 0
        self.NS_total = 0
        self.EW_score = 0
        self.EW_total = 0
        self.Q = False
        self.K = False
        self.bel = False
        self.rebel = False
        self.belote_rebelote = False
        self.br_player = None
        self.dix_de_der = None
        self.new_number_order = None
        self.eigth_turn = 8
        self.iterator = 0

        self.north_place = 0
        self.worst_card = None
        self.delete = 0
        self.worst_trump = None
        self.color_possession = False

        self.show_north = True

    def playing(self):
        #print(f"number_order : {self.number_order}")
        self.new_number_order = self.number_order
        Distribution.update_dist(self)
        if self.new_trump_color is not None:
            self.belote_reb()
            for i in range(self.eigth_turn):
                self.trump_on_the_board = False
                self.play_ok = False
                self.highest_trump = None
                self.show_north = True
                #print(f"play_card debut : {self.play_card}")
                #print(self.number_order)
                if self.azimuth[self.north_place] == "North":
                    print(f"{self.azimuth[self.number_order[0]]} : {self.player_number[0]}")
                    self.choose_card = int(input("Quelle carte voulez-vous jouer? (entrer le numéro de la carte) : "))
                    self.play_card = self.player_number[0][self.choose_card - 1]
                    if list(self.play_card.keys())[0][1] == self.new_trump_color:
                        self.trump_on_the_board = True
                        self.highest_trump = self.play_card
                    del self.player_number[0][self.choose_card - 1]
                else:
                    #print(f"{self.azimuth[self.number_order[0]]} : {self.player_number[0]}")
                    for j in range(len(self.player_number[0])):
                        #print(list(self.player_number[0][j].keys())[0][0], list(self.player_number[0][j].keys())[0][1])
                        if self.trump_player == j and self.player_number[0][j] == {('J', self.new_trump_color): 20}:
                            self.play_card = self.player_number[0][j]
                            self.play_ok = True
                            self.delete = j
                        elif list(self.player_number[0][j].keys())[0][0] == "As" and list(self.player_number[0][j].keys())[0][1] != self.new_trump_color:
                            self.play_card = self.player_number[0][j]
                            self.play_ok = True
                            self.delete = j
                        elif j == len(self.player_number[0]) - 1:
                            self.worst_card = self.player_number[0][0]
                            self.delete = 0
                            for kk in range(1, len(self.player_number[0])):
                                if list(self.player_number[0][kk].keys())[0][1] != self.new_trump_color and list(self.player_number[0][kk].values()) < list(self.worst_card.values()):
                                    self.worst_card = self.player_number[0][kk]
                                    self.delete = kk
                            self.play_ok = True
                            self.play_card = self.worst_card
                            break
                    del self.player_number[0][self.delete]
                self.play_ok = False
                if list(self.play_card.keys())[0][1] == self.new_trump_color:
                    self.trump_on_the_board = True
                    self.highest_trump = self.play_card
                print(self.play_card)
                if self.belote_rebelote and self.bel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                    print("Rebelote")
                    self.bel = False
                if self.belote_rebelote and self.rebel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                    print("Belote")
                    self.bel = True
                    self.rebel = False
                self.actual_turn.append(self.play_card)
                self.play_color = list(self.play_card.keys())[0][1]
                for j in range(1, 4):
                    self.trump_possession = False
                    self.play_ok = False
                    self.test = False
                    self.color_possession = False
                    for k in range(len(self.player_number[j])):
                        for kk in range(len(self.player_number[j])):
                            if list(self.player_number[j][kk].keys())[0][1] == self.play_color and self.play_color != self.new_trump_color:
                                self.color_possession = True
                            if list(self.player_number[j][kk].keys())[0][1] == self.new_trump_color:
                                self.trump_possession = True
                        #print(f"self.color possession {self. color_possession}")
                        if self.trump_possession and self.play_color == self.new_trump_color:
                            print(f"Jouez du {self.new_trump_color} pour couper")
                            #print(self.trump_on_the_board)
                        if self.azimuth[self.number_order[j]] == "North":
                            if self.show_north:
                                print(f"{self.azimuth[self.number_order[j]]} : {self.player_number[j]}")
                                self.show_north = False
                            trump = 0
                            if list(self.player_number[j][k].keys())[0][1] == self.play_color and self.play_color != self.new_trump_color :
                                print(f"Jouez du {self.play_color}")
                                self.playing_test(j, self.play_color)
                                self.play_ok = True
                                break
                            if self.highest_trump is not None and self.trump_possession:
                                while not self.play_ok and trump < len(self.player_number[j]):
                                    if list(self.player_number[j][trump].values()) > list(self.highest_trump.values()):
                                        print("Surenchérir avec un atout plus élevé : ")
                                        self.playing_test(j, self.new_trump_color)
                                        while list(self.play_card.values()) < list(self.highest_trump.values()):
                                            print("Il est obligatoire de surenchérir")
                                            self.playing_test(j, self.new_trump_color)
                                        self.highest_trump = self.play_card
                                        if self.belote_rebelote and self.bel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                            print("Rebelote")
                                            self.bel = False
                                        if self.belote_rebelote and self.rebel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                            print("Belote")
                                            self.bel = True
                                            self.rebel = False
                                        self.play_ok = True
                                    trump += 1
                                if trump == len(self.player_number[j])-1:
                                    self.test = True
                            if self.play_ok:
                                break
                                #cas si le joueur ne possède que le 8 dû à leur valeur identitque
                            if self.test and not self.play_ok and self.trump_possession:
                                for trump in range(len(self.player_number[j])):
                                    if list(self.highest_trump.keys())[0][0] == '7':
                                        print("Surenchérir avec un atout plus élevé : ")
                                        self.playing_test(j, self.new_trump_color)
                                    else:
                                        print("Défaussez-vous d'un atout : ")
                                        self.playing_test(j, self.new_trump_color)
                                    if self.belote_rebelote and self.bel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                        print("Rebelote")
                                        self.bel = False
                                    if self.belote_rebelote and self.rebel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                        print("Belote")
                                        self.bel = True
                                        self.rebel = False
                                    break
                                if not self.play_ok:
                                    self.test = False
                                    break
                            if self.trump_possession and self.play_color != self.new_trump_color and k == len(self.player_number[j])-1:
                                print("condition defausse")
                                #pint(self.azimuth[self.first_player])
                                #print(self.azimuth[self.number_order[j]])
                                if self.azimuth[self.number_order[j]] == "North" and self.azimuth[self.first_player] == "South":
                                    print("Votre partenaire est maître, vous n'êtres pas obligé de couper")
                                    self.default_play(j)
                                elif self.azimuth[self.number_order[j]] == "South" and self.azimuth[self.first_player] == "North":
                                    print("Votre partenaire est maître, vous n'êtres pas obligé de couper")
                                    self.default_play(j)
                                elif self.azimuth[self.number_order[j]] == "East" and self.azimuth[self.first_player] == "West":
                                    print("Votre partenaire est maître, vous n'êtres pas obligé de couper")
                                    self.default_play(j)
                                elif self.azimuth[self.number_order[j]] == "West" and self.azimuth[self.first_player] == "East":
                                    print("Votre partenaire est maître, vous n'êtres pas obligé de couper")
                                    self.default_play(j)
                                else:
                                    print(f"Jouez du {self.new_trump_color} pour couper")
                                    self.playing_test(j, self.new_trump_color)
                                    self.highest_trump = self.play_card
                                    self.trump_on_the_board = True
                                if self.belote_rebelote and self.bel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                    print("Rebelote")
                                    self.bel = False
                                if self.belote_rebelote and self.rebel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                    print("Belote")
                                    self.bel = True
                                    self.rebel = False
                                break
                            if k == len(self.player_number[j]) - 1 and \
                                    list(self.player_number[j][k].keys())[0][1] != self.play_color and not self.trump_possession:
                                print(f"Défaussez-vous d'une carte")
                                self.default_play(j)
                                break
                        else:
                            if list(self.player_number[j][k].keys())[0][1] == self.play_color and self.play_color != self.new_trump_color and self.color_possession:
                                if list(self.player_number[j][k].keys())[0][0] == "As" and list(self.player_number[j][k].keys())[0][1] != self.new_trump_color:
                                    self.play_card = self.player_number[j][k]
                                    self.play_ok = True
                                    self.delete = k
                                else:
                                    count = 0
                                    for kk in range(len(self.player_number[j])):
                                        if list(self.player_number[j][kk].keys())[0][1] != self.new_trump_color:
                                            if count == 0 and list(self.player_number[j][kk].keys())[0][1] == self.play_color:
                                                self.worst_card = self.player_number[j][kk]
                                                self.play_card = self.worst_card
                                                count += 1
                                                self.delete = kk
                                            elif count > 0 and list(self.player_number[j][kk].keys())[0][1] == self.play_color:
                                                if list(self.worst_card.values()) > list(self.player_number[j][kk].values()):
                                                    self.worst_card = self.player_number[j][kk]
                                                    self.play_card = self.worst_card
                                                    #count += 1
                                                    self.delete = kk
                                    self.play_ok = True
                            if self.play_ok:
                                del self.player_number[j][self.delete]
                                break
                            trump = 0
                            if self.highest_trump is not None and k == len(self.player_number[j]) - 1 and self.play_color == self.new_trump_color and self.trump_possession:
                                while not self.play_ok and trump < len(self.player_number[j]):
                                    if list(self.player_number[j][k].keys())[0][1] == self.new_trump_color and list(self.player_number[j][k].values()) > list(self.highest_trump.values()):
                                        self.highest_trump = self.player_number[j][k]
                                        self.play_card = self.player_number[j][k]
                                        self.play_ok = True
                                        self.delete = k
                                    if list(self.player_number[j][k].keys())[0][0] == 'J' and list(self.player_number[j][k].keys())[0][1] == self.new_trump_color:
                                        self.highest_trump = self.player_number[j][k]
                                        self.play_card = self.player_number[j][k]
                                        self.play_ok = True
                                        self.delete = k
                                    if self.belote_rebelote and self.bel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                        print("Rebelote")
                                        self.bel = False
                                    if self.belote_rebelote and self.rebel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                        print("Belote")
                                        self.bel = True
                                        self.rebel = False
                                    trump += 1
                                    if trump == len(self.player_number[j]) - 1:
                                        self.test = True
                            if self.play_ok:
                                del self.player_number[j][self.delete]
                                break
                                # cas si le joueur ne possède que le 8 dû à leur valeur identitque
                            if not self.play_ok and not self.color_possession and self.play_color == self.new_trump_color and self.trump_possession:
                                if self.highest_trump is not None:
                                    if list(self.highest_trump.keys())[0][0] == '7':
                                        if list(self.player_number[j][k].keys())[0][1] == self.new_trump_color and list(self.player_number[j][k].values()) > list(self.highest_trump.values()):
                                            self.highest_trump = self.player_number[j][k]
                                            self.play_card = self.player_number[j][k]
                                            self.play_ok = True
                                            self.delete = k
                                    else:
                                        self.worst_trump = self.highest_trump
                                        for kk in range(len(self.player_number[j])):
                                            if list(self.player_number[j][kk].keys())[0][1] == self.new_trump_color and list(self.player_number[j][kk].values()) < list(self.worst_trump.values()):
                                                self.worst_trump = self.player_number[j][kk]
                                                self.play_card = self.worst_trump
                                                self.play_ok = True
                                                self.delete = kk
                                if self.bel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                    if self.belote_rebelote and self.bel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                        print("Rebelote")
                                        self.bel = False
                                    if self.belote_rebelote and self.rebel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                        print("Belote")
                                        self.bel = True
                                        self.rebel = False
                            if self.trump_possession and self.play_color != self.new_trump_color and k == len(self.player_number[j]) - 1 and not self.play_ok and not self.color_possession:
                                #print("condition defausse")
                                #print(self.azimuth[self.first_player])
                                #print(self.azimuth[self.number_order[j]])
                                if self.azimuth[self.number_order[j]] == "North" and self.azimuth[self.first_player] == "South":
                                    self.play_card = self.player_number[j][0]
                                    self.delete = 0
                                    if list(self.player_number[j][k].keys())[0][1] != self.new_trump_color and list(self.player_number[j][k].values()) == 10:
                                        self.play_card = self.player_number[j][k]
                                        self.play_ok = True
                                        self.delete = k
                                    else:
                                        self.play_card = self.player_number[j][0]
                                        self.delete = 0
                                        if list(self.play_card.values()) > list(self.player_number[j][k].values()):
                                            self.play_card = self.player_number[j][k]
                                            self.delete = k
                                            if k == len(self.player_number[j]):
                                                self.play_ok = True
                                elif self.azimuth[self.number_order[j]] == "South" and self.azimuth[self.first_player] == "North":
                                    self.play_card = self.player_number[j][0]
                                    self.delete = 0
                                    if list(self.player_number[j][k].keys())[0][1] != self.new_trump_color and list(
                                            self.player_number[j][k].values()) == 10:
                                        self.play_card = self.player_number[j][k]
                                        self.play_ok = True
                                        self.delete = k
                                    else:
                                        self.play_card = self.player_number[j][0]
                                        self.delete = 0
                                        if list(self.play_card.values()) > list(self.player_number[j][k].values()):
                                            self.play_card = self.player_number[j][k]
                                            self.delete = k
                                            if k == len(self.player_number[j]):
                                                self.play_ok = True
                                elif self.azimuth[self.number_order[j]] == "East" and self.azimuth[self.first_player] == "West":
                                    self.play_card = self.player_number[j][0]
                                    self.delete = 0
                                    if list(self.player_number[j][k].keys())[0][1] != self.new_trump_color and list(
                                            self.player_number[j][k].values()) == 10:
                                        self.play_card = self.player_number[j][k]
                                        self.play_ok = True
                                        self.delete = k
                                    else:
                                        self.play_card = self.player_number[j][0]
                                        self.delete = 0
                                        if list(self.play_card.values()) > list(self.player_number[j][k].values()):
                                            self.play_card = self.player_number[j][k]
                                            self.delete = k
                                            if k == len(self.player_number[j]):
                                                self.play_ok = True
                                elif self.azimuth[self.number_order[j]] == "West" and self.azimuth[self.first_player] == "East":
                                    self.play_card = self.player_number[j][0]
                                    self.delete = 0
                                    if list(self.player_number[j][k].keys())[0][1] != self.new_trump_color and list(self.player_number[j][k].values()) == 10:
                                        self.play_card = self.player_number[j][k]
                                        self.play_ok = True
                                        self.delete = k
                                    else:
                                        self.play_card = self.player_number[j][0]
                                        self.delete = 0
                                        if list(self.play_card.values()) > list(self.player_number[j][k].values()):
                                            self.play_card = self.player_number[j][k]
                                            self.delete = k
                                            if k == len(self.player_number[j]):
                                                self.play_ok = True
                                else:
                                    print("coupe")
                                    for kk in range(len(self.player_number[j])):
                                        if list(self.player_number[j][kk].keys())[0][1] == self.new_trump_color:
                                            self.play_card = self.player_number[j][kk]
                                            self.highest_trump = self.play_card
                                            self.trump_on_the_board = True
                                            self.delete = kk
                                            self.play_ok = True
                                        if self.play_ok:
                                            del self.player_number[j][self.delete]
                                            break
                                if self.belote_rebelote and self.bel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                    print("Rebelote")
                                    self.bel = False
                                if self.belote_rebelote and self.rebel and (list(self.play_card.keys())[0][0] == "Q" or list(self.play_card.keys())[0][0] == 'K'):
                                    print("Belote")
                                    self.bel = True
                                    self.rebel = False
                                break
                            if self.play_ok:
                                del self.player_number[j][self.delete]
                                break
                            if k == len(self.player_number[j]) - 1 and list(self.player_number[j][k].keys())[0][1] != self.play_color and not self.trump_possession and not self.color_possession:
                                print("défausse")
                                self.play_card = self.player_number[j][0]
                                for kk in range(len(self.player_number[j])):
                                    if list(self.play_card.values()) > list(self.player_number[j][kk].values()):
                                        self.play_card = self.player_number[j][kk]
                                        self.delete = kk
                                        self.play_ok = True
                                if self.play_ok:
                                    del self.player_number[j][self.delete]
                                    break
                            if self.play_ok:
                                break
                    #print(f"self.trump_possession = {self.trump_possession}")
                    #print(self.play_card)
                    self.actual_turn.append(self.play_card)
                    print(self.actual_turn)
                    self.power_of_cards()
                #print("exit loop")
                self.power_of_cards()
                self.folds(self.actual_turn)
                self.actual_turn = []
                self.turn()
                if i == self.eigth_turn - 1:
                    self.dix_de_der = self.azimuth[self.first_player]
                    self.score()

    def playing_test(self, ite, test):
        self.choose_card = int(input("Quelle carte voulez-vous jouer? "
                                     "(entrer le numéro de la carte) : "))
        self.play_card = self.player_number[ite][self.choose_card - 1]
        while list(self.play_card.keys())[0][1] != test:
            self.choose_card = int(input(f"Vous possédez du {test}\n"
                                         f"Jouez une carte adéquat : "))
            self.play_card = self.player_number[ite][self.choose_card - 1]
        del self.player_number[ite][self.choose_card - 1]
        return self.play_card

    def default_play(self, ite):
        self.choose_card = int(input("Quelle carte voulez-vous jouer? "
                                     "(entrer le numéro de la carte) : "))
        self.play_card = self.player_number[ite][self.choose_card - 1]
        del self.player_number[ite][self.choose_card - 1]
        self.test = True
        return self.play_card

    def belote_reb(self):
        for i in range(4):
            for j in range(8):
                if list(self.player_number[i][j].keys())[0][1] == self.new_trump_color and list(self.player_number[i][j].keys())[0][0] == 'Q':
                    self.Q = True
                if list(self.player_number[i][j].keys())[0][1] == self.new_trump_color and list(self.player_number[i][j].keys())[0][0] == 'K':
                    self.K = True
                if self.Q and self.K:
                    self.belote_rebelote = True
                    self.rebel = True
                    self.br_player = i
                    self.br_player = self.azimuth[self.br_player]
                    break
            self.Q = False
            self.K = False
        #print(f"br : {self.belote_rebelote}")
        return self.belote_rebelote

    def power_of_cards(self):
        self.most_powerful_card = self.actual_turn[0]
        #print('in power of card')
        for i in range(len(self.actual_turn)):
            if list(self.most_powerful_card.keys())[0][1] != self.new_trump_color and \
                    list(self.actual_turn[i].keys())[0][1] != self.new_trump_color and \
                    list(self.actual_turn[i].keys())[0][1] == self.play_color:
                if list(self.most_powerful_card.values()) < list(self.actual_turn[i].values()):
                    self.most_powerful_card = self.actual_turn[i]
                    self.first_player = self.number_order[i]
                if list(self.most_powerful_card.values()) == list(self.actual_turn[i].values()):
                    if list(self.actual_turn[i].keys())[0][0] == '9':
                        self.most_powerful_card = self.actual_turn[i]
                        self.first_player = self.number_order[i]
                    elif list(self.actual_turn[i].keys())[0][0] == '8' and list(self.most_powerful_card.keys())[0][0] != '9':
                        self.most_powerful_card = self.actual_turn[i]
                        self.first_player = self.number_order[i]
            if list(self.most_powerful_card.keys())[0][1] == self.new_trump_color and \
                    list(self.actual_turn[i].keys())[0][1] == self.new_trump_color:
                if list(self.most_powerful_card.values()) < list(self.actual_turn[i].values()):
                    self.most_powerful_card = self.actual_turn[i]
                    self.first_player = self.number_order[i]
                if list(self.most_powerful_card.values()) == list(self.actual_turn[i].values()):
                    if list(self.actual_turn[i].keys())[0][0] == '8':
                        self.most_powerful_card = self.actual_turn[i]
                        self.first_player = self.number_order[i]
            if list(self.most_powerful_card.keys())[0][1] != self.new_trump_color and \
                    list(self.actual_turn[i].keys())[0][1] == self.new_trump_color:
                self.most_powerful_card = self.actual_turn[i]
                self.first_player = self.number_order[i]
        if len(self.actual_turn) == 4:
            self.first_player_position = self.number_order.index(self.first_player)
            #print(self.most_powerful_card)
            print(f"{self.azimuth[self.first_player]} commence ce tour")
            #print(f"first_player_position : {self.first_player_position}")
            print(self.actual_turn)
            self.fold.append(self.actual_turn)
            self.fold_winner = self.azimuth[self.first_player]
            print(self.fold)
        return self.most_powerful_card

    def turn(self):
        self.next_order = []
        self.next_number_order = []
        self.next_order.append(self.player_number[self.first_player_position])
        self.next_number_order.append(self.first_player)
        self.next_player = self.first_player + 1
        self.next_player_position = self.first_player_position + 1
        while len(self.next_order) < 4:
            if self.next_player_position < 4:
                self.next_order.append(self.player_number[self.next_player_position])
                self.next_player_position += 1
            if self.next_player_position == 4:
                self.next_player_position = 0
            if self.next_player_position < self.first_player_position:
                self.next_order.append(self.player_number[self.next_player_position])
                self.next_player_position += 1
        while len(self.next_number_order) < 4:
            if self.next_player < 4:
                self.next_number_order.append(self.next_player)
                self.next_player += 1
            if self.next_player == 4:
                self.next_player = 0
            if self.next_player < self.first_player_position:
                self.next_number_order.append(self.next_player)
                self.next_player += 1
        self.player_number = self.next_order
        self.number_order = self.next_number_order
        self.north_place = self.number_order.index(0)
        return self.player_number, self.next_number_order

    def folds(self, actual_turn):
        #print("in folds")
        if self.fold_winner == "North" or self.fold_winner == "South":
            self.NS_fold.append(list(actual_turn))
            print(f"NS : {self.NS_fold}")
            #print(actual_turn)
        if self.fold_winner == "East" or self.fold_winner == "West":
            self.EW_fold.append(list(actual_turn))
            print(f"EW : {self.EW_fold}")
            #print(actual_turn)

    def score(self):
        print((f"NSfolds : {self.NS_fold}"))
        print((f"EWfolds : {self.EW_fold}"))
        if len(self.NS_fold) < 8:
            for i in range(len(self.NS_fold)):
                for j in range(4):
                    self.NS_score += list(self.NS_fold[i][j].values())[0]
        if self.dix_de_der == "North" or self.dix_de_der == "South":
            self.NS_score += 10
        self.NS_total += self.NS_score
        if self.belote_rebelote and (self.br_player == "North" or self.br_player == "South"):
            self.NS_total += 20
        if len(self.EW_fold) < 8:
            for i in range(len(self.EW_fold)):
                for j in range(4):
                    self.EW_score += list(self.EW_fold[i][j].values())[0]
        if self.dix_de_der == "East" or self.dix_de_der == "West":
            self.EW_score += 10
        self.EW_total += self.EW_score
        if self.belote_rebelote and (self.br_player == "East" or self.br_player == "West"):
            self.EW_total += 20
        if len(self.NS_fold) == 8 and (self.trump_player == 0 or self.trump_player == 2):
            self.NS_total += 252
        if len(self.NS_fold) == 8 and (self.trump_player == 1 or self.trump_player == 3):
            self.NS_total += 252
        if self.NS_score < 82 and (self.trump_player == 0 or self.trump_player == 2):
            self.NS_total -= self.NS_score
            self.EW_total += 162 - self.EW_score
        if self.EW_score < 82 and (self.trump_player == 1 or self.trump_player == 3):
            self.EW_total -= self.EW_score
            self.NS_total += 162 - self.NS_score
        print(f"Score de NS : {self.NS_score}, score total : {self.NS_total}")
        print(f"Score de EW : {self.EW_score}, score total : {self.EW_total}")
        return self.NS_total, self.EW_total

    def new_game(self):
        self.shuffle_deck = []
        for i in range(len(self.NS_fold)):
            for j in range(4):
                self.shuffle_deck.append(self.NS_fold[i][j])
        for i in range(len(self.EW_fold)):
            for j in range(4):
                self.shuffle_deck.append(self.EW_fold[i][j])
        #self.shuffle_deck = self.NS_fold + self.EW_fold
        #print(f"newshuffl : {self.shuffle_deck}")
        for i in range(self.nb_players):
            self.player_number = [Player.players(self) for i in range(self.nb_players)]
        self.second_dist = False
        self.Q = False
        self.K = False
        self.belote_rebelote = False
        self.br_player = None
        self.NS_fold = []
        self.EW_fold = []
        self.NS_score = 0
        self.EW_score = 0
        self.nine_pos = self.shuffle_deck.index({('9', self.new_trump_color): 14})
        self.shuffle_deck[self.nine_pos][('9', self.new_trump_color)] = 0
        self.jack_pos = self.shuffle_deck.index({('J', self.new_trump_color): 20})
        self.shuffle_deck[self.jack_pos][('J', self.new_trump_color)] = 2
        self.iterator += 1
        if self.iterator == 4:
            self.iterator = 0
        save_iterator = self.iterator
        self.number_order = []
        while len(self.number_order) < 4:
            if save_iterator < 4:
                self.number_order.append(self.new_number_order[save_iterator])
                save_iterator += 1
            if save_iterator == 4:
                save_iterator = 0
            if save_iterator < self.iterator:
                self.number_order.append(self.new_number_order[save_iterator])
                save_iterator += 1
        return self.shuffle_deck

    def reinitialisation(self):
        for i in range(self.nb_players):
            self.player_number = [Player.players(self) for i in range(self.nb_players)]
        self.second_dist = False
        self.Q = False
        self.K = False
        self.belote_rebelote = False
        self.br_player = None
        self.NS_fold = []
        self.EW_fold = []
        self.NS_score = 0
        self.EW_score = 0
        if self.iterator == 4:
            self.iterator = 0
        save_iterator = self.iterator
        self.number_order = []
        while len(self.number_order) < 4:
            if save_iterator < 4:
                self.number_order.append(self.new_number_order[save_iterator])
                save_iterator += 1
            if save_iterator == 4:
                save_iterator = 0
            if save_iterator < self.iterator:
                self.number_order.append(self.new_number_order[save_iterator])
                save_iterator += 1
