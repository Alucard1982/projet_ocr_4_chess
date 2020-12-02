from controleur.controleur import ControleurTournementProgress
from vue.view import IhmMenu
from modele.joueur import Player
from modele.tournois import Tournement
from tinydb import TinyDB


class ControleurMenu:

    def __init__(self):
        pass

    def description_tournement(self):
        tournois = Tournement()
        list_choix_tournement = IhmMenu.menu_description_tournement()
        if list_choix_tournement[0]:
            tournois.name = list_choix_tournement[0]
        elif list_choix_tournement[1]:
            tournois.location = list_choix_tournement[1]
        elif list_choix_tournement[2]:
            tournois.date = list_choix_tournement[2]
        elif list_choix_tournement[3]:
            tournois.time_control = list_choix_tournement[3]
        elif list_choix_tournement[4]:
            tournois.description = list_choix_tournement[4]
        return tournois

    def description_player(self):
        list_players = []
        for i in range(8):
            player = Player()
            list_choix = IhmMenu.menu_entrer_joueur()
            if list_choix[0]:
                player.first_name = list_choix[0]
            if list_choix[1]:
                player.last_name = list_choix[1]
            if list_choix[2]:
                player.date_of_birth = list_choix[2]
            if list_choix[3]:
                player.sex = list_choix[3]
            if list_choix[4]:
                player.ranking = list_choix[4]
            if list_choix[5]:
                player.id_player = list_choix[5]
            list_players.append(player)
        return list_players

    def chess_tournement(self):
        controleur = ControleurTournementProgress()
        round1 = controleur.pair_players_round1()
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
        print(final_ranking)
        list_round = [round1, round2, round3, round4]
        return list_round

    def tournement_software(self):
        tournois = self.description_tournement()
        # list_players = self.description_player
        controleur = ControleurTournementProgress()
        list_players = controleur.create_players()
        for player in list_players:
            tournois.add_player(player)
        IhmMenu.menu_generale()
        choice_menu_generale = int(input(" Choisissez une action : --> "))
        if choice_menu_generale == 1:
            list_rounds = self.chess_tournement()
            for rounde in list_rounds:
                tournois.add_round(rounde)

        if choice_menu_generale == 2:
            pass
        if choice_menu_generale == 3:
            print("BYEEEEEEEEEEEEEEEEE")