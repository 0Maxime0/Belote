# Belote

Jeu de carte de la Belote

Instructions
============

Le jeu s'exécute à partir du fichier main.py associer aux autres fichiers présents.

Comment jouer 
====

* Vous serez le joueur nommé North et vous commencerz la partie
* Le autres joueurs jouerons automatiquement
* Le jeu va vous proposer montrer vos 5 premières cartes et vous proposer une carte d'atout
* Si la carte vous intéressé par la carte, taper `Y`
```
self.trump_card : {('As', 'spade'): 11}
actual trump color : spade
trump : {('As', 'spade'): 11}
Voulez vous cette carte comme atout : spade(Y/N) :Y
...
```
* Le jeu commence ensuite en affichant vos cartes
* Jouer une carte en tapant un numbre de 1 à 8 au clavier 1 étant la première carte et 8 la dernière
* Le nombre maximal de carte diminuera au fil de la partie passant de 8 à 7 à 6 ...
* Lorsque vous gagnez vous êtes une nouvelle fois le premier joueur du tour
* Si un autre joueur gagne le tour, le gagnant jouera une carte de son choix et il faudra respecter la règle du jeu (jouer la même couleur, sinon couper, sinon se défausser...)
* Une aide s'affichera : exemple avec une coupe
```
cartes sur la table : {('9', 'clover'): 0}
North : [{('K', 'heart'): 4}, {('9', 'diamond'): 0}, {('As', 'heart'): 11}, {('J', 'spade'): 20}, {('As', 'spade'): 11}, {('8', 'spade'): 0}, {('7', 'spade'): 0}]
condition defausse
Jouez du spade pour couper
Quelle carte voulez-vous jouer? (entrer le numéro de la carte) : 
...
```
* La partie se termine une fois les 500 points atteint par une équipe
