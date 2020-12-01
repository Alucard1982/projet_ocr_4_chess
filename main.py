from controleur.controleur import Controleur
from vue.view import IhmMenu
from modele.joueur import Player

if __name__ == '__main__':
    controleur= Controleur()
    controleur.create_players()

    round1 = controleur.pair_players_round1()
    list_scored_player = controleur.scored_match_round1(round1)

    controleur.pair_player_round2(list_scored_player)

"""joueur = Player()


list_choix = IhmMenu.menu_entrer_joueur()
if list_choix[0]:
    joueur.first_name = list_choix[0]
if list_choix[1]:
    joueur.last_name = list_choix[1]

print(joueur)"""
