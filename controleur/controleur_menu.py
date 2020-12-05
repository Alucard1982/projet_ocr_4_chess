from controleur.controleur import ControleurTournementProgress
from vue.view import IhmMenu
from modele.joueur import Player
from modele.tournois import Tournement
from tinydb import TinyDB
from operator import itemgetter


class ControleurMenu:

    """def __init__(self):
        pass"""

    @staticmethod
    def description_tournement():
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

    @staticmethod
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

    @staticmethod
    def chess_tournement():
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
        final_ranking = controleur.scored_match_round4(round4)
        IhmMenu.print_string("***************FINAL RANKING******************\n")
        IhmMenu.print_string(final_ranking)
        list_round = (round1, round2, round3, round4)
        return list_round

    @staticmethod
    def tournement_software(self):
        boole = True
        while boole:
            IhmMenu.menu_generale()
            choice_menu_generale = IhmMenu.saisie_int(" Choisissez une action : --> ")
            if choice_menu_generale == 1:
                tournois = self.description_tournement()
                # list_players = self.description_player
                controleur = ControleurTournementProgress()
                list_players = controleur.create_players()
                list_rounds = self.chess_tournement()
                db = TinyDB('db.json')
                players_table = db.table('players')
                list_dic_player = []
                list_dic_round = []
                list_dic_match = []
                for player in list_players:
                    tournois.add_player(player)
                    player_dic = player.to_dict()
                    players_table.insert(player_dic)
                    list_dic_player.append(player_dic)
                for rounde in list_rounds:
                    tournois.add_round(rounde)
                    dic_round = {'name_round': rounde.name, "start_date": rounde.star_date,
                                 "end_date": rounde.end_date}
                    list_dic_round.append(dic_round)
                    for match in rounde.list_match:
                        dic_player1_match = match[0][0].to_dict()
                        dic_player2_match = match[1][0].to_dict()
                        dic_match = {"player1": dic_player1_match, "score_player1": match[0][1],
                                     "player2": dic_player2_match, "score_player2": match[1][1]}
                        list_dic_match.append(dic_match)
                tournement_table = db.table('tournement')
                tournement_table.insert({'name_tournement': tournois.name, 'location': tournois.location,
                                         'date': tournois.date, 'nb_round': tournois.nb_round,
                                         'time_control': tournois.time_control, 'description': tournois.description,
                                         'list_player': list_dic_player, 'list_round': list_dic_round,
                                         'list_match': list_dic_match})
            if choice_menu_generale == 2:
                self.report()
            if choice_menu_generale == 3:
                boole = False
                IhmMenu.print_string("THX FOR PLAYING CHESS!! HAVE A NICE DAY")

    @staticmethod
    def report(self):
        boole = True
        db = TinyDB('db.json')
        players_table = db.table('players')
        tournement_table = db.table('tournement')
        while boole:
            IhmMenu.menu_rapport()
            choice_menu_report = IhmMenu.saisie_int(" Choisissez une action : --> ")
            if choice_menu_report == 1:
                list_players = sorted(players_table.all(), key=itemgetter('first_name'))
                for player in list_players:
                    IhmMenu.print_string(player)
            if choice_menu_report == 2:
                list_players = sorted(players_table.all(), key=itemgetter('ranking'), reverse=True)
                for player in list_players:
                    IhmMenu.print_string(player)
            if choice_menu_report == 3:
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    IhmMenu.print_string("Tournement " + tournois[i]['name_tournement'] + ":")
                    list_players = sorted(tournois[i]['list_player'], key=itemgetter('first_name'))
                    for player in list_players:
                        IhmMenu.print_string(player)
            if choice_menu_report == 4:
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    IhmMenu.print_string("Tournement " + tournois[i]['name_tournement'] + ":")
                    list_players = sorted(tournois[i]['list_player'], key=itemgetter('ranking'), reverse=True)
                    for player in list_players:
                        IhmMenu.print_string(player)
            if choice_menu_report == 5:
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    IhmMenu.print_string(
                        tournois[i]['name_tournement'] + "," + tournois[i]['location'] + "," + tournois[i]['date'] +
                        str(tournois[i]['nb_round']) + "," + tournois[i]['time_control'] + "," +
                        tournois[i]['description'])
            if choice_menu_report == 6:
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    IhmMenu.print_string("Tournement " + tournois[i]['name_tournement'] + ":")
                    list_rounds = tournois[i]['list_round']
                    for round in list_rounds:
                        IhmMenu.print_string(round)
            if choice_menu_report == 7:
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    IhmMenu.print_string("Tournement " + tournois[i]['name_tournement'] + ":")
                    list_match = tournois[i]['list_match']
                    for match in list_match:
                        IhmMenu.print_string(match)
            if choice_menu_report == 8:
                boole = False
