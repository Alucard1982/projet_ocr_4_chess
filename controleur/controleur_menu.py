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
        if list_choix_tournement[1]:
            tournois.location = list_choix_tournement[1]
        if list_choix_tournement[2]:
            tournois.date = list_choix_tournement[2]
        if list_choix_tournement[3]:
            tournois.time_control = list_choix_tournement[3]
        if list_choix_tournement[4]:
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
        IhmMenu.print_string("*******************ROUND1******************\n")
        round1 = controleur.pair_players_round1()
        IhmMenu.print_string(round1.list_match)
        list_scored_player = controleur.scored_match_round1(round1)
        IhmMenu.print_string(list_scored_player)
        IhmMenu.print_string("*******************ROUND2******************\n")
        round2 = controleur.pair_player_round2(list_scored_player)
        IhmMenu.print_string(round2.list_match)
        list_scored_player_round2 = controleur.scored_match_round2(round2)
        IhmMenu.print_string(list_scored_player_round2)
        IhmMenu.print_string("*******************ROUND3******************\n")
        round3 = controleur.pair_player_round3(list_scored_player_round2)
        IhmMenu.print_string(round3.list_match)
        list_scored_player_round3 = controleur.scored_match_round3(round3)
        IhmMenu.print_string(list_scored_player_round3)
        IhmMenu.print_string("*******************ROUND4******************\n")
        round4 = controleur.pair_player_round4(list_scored_player_round3)
        IhmMenu.print_string(round4.list_match)
        final_ranking = controleur.scored_match_round3(round4)
        IhmMenu.print_string("***************FINAL RANKING******************\n")
        IhmMenu.print_string(final_ranking)
        list_round = (round1, round2, round3, round4)
        return list_round

    def tournement_software(self):
        boole = True
        while boole:
            IhmMenu.menu_generale()
            choice_menu_generale = int(input(" Choisissez une action : --> "))
            if choice_menu_generale == 1:
                tournois = self.description_tournement()
                # list_players = self.description_player
                controleur = ControleurTournementProgress()
                list_players = controleur.create_players()
                list_rounds = self.chess_tournement()
                db = TinyDB('db.json')
                players_table = db.table('players')
                list_dic_player = []
                list_dic_match = []
                list_dic_round = []
                for player in list_players:
                    tournois.add_player(player)
                    dic_player = {'first_name': player.first_name, 'last_name': player.last_name,
                                  'date_of_birth': player.date_of_birth, 'sex': player.sex,
                                  'ranking': player.ranking}
                    players_table.insert(dic_player)
                    list_dic_player.append(dic_player)
                """ for rounde in list_rounds:
                    tournois.add_round(rounde)
                    list_dic_round ={'name_round': rounde.name, 'star_date': rounde.star_date,
                                             'end_date': rounde.end_date}
                    list_dic_round.append(list_dic_round)
                    i = 0
                        for match in rounde.list_match:
                            i = i+1
                            dic_match = {"match"+str(i): match}
                            list_dic_match.append(dic_match)
                    print(list_dic_match)"""
                tournement_table = db.table('tournement')
                tournement_table.insert({'name_tournement': tournois.name, 'location': tournois.location,
                                         'date': tournois.date,
                                         'nb_round': tournois.nb_round,
                                         'time_control': tournois.time_control,
                                         'description': tournois.description,
                                         'list_player': list_dic_player,
                                         #'list_round' : list_dic_round,
                                         #'list_match': list_dic_match,
                                         })
                """
                    tournement_table.insert({'name_round': rounde.name, 'star_date': rounde.star_date,
                                             'end_date': rounde.end_date})"""

            if choice_menu_generale == 3:
                boole = False
                IhmMenu.print_string("THX FOR PLAYING CHESS!! HAVE A NICE DAY")

    def report(self):
        pass
