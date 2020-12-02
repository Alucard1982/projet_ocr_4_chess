from controleur.controleur import ControleurTournementProgress
from vue.view import IhmMenu
from modele.joueur import Player
from controleur.controleur_menu import ControleurMenu

if __name__ == '__main__':

    """round1 = controleur.pair_players_round1()
        list_scored_player = controleur.scored_match_round1(round1)
        print(list_scored_player)

        round2 = controleur.pair_player_round2(list_scored_player)
        list_scored_player_round2 = controleur.scored_match_round2(round2)
        print(list_scored_player_round2)

        round3 = controleur.pair_player_round3(list_scored_player_round2)
        list_scored_player_round3 = controleur.scored_match_round3(round3)
        print(list_scored_player_round3)

        round4 = controleur.pair_player_round4(list_scored_player_round3)
        final_ranking = controleur.scored_match_round3(round4)
        print(final_ranking)"""

    controleur = ControleurMenu()
    controleur.tournement_software()





