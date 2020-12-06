from vue.view import IhmMenu
from modele.joueur import Player
from modele.tournois import Tournement
from tinydb import TinyDB
from operator import itemgetter


class ControleurMenu:
    def __init__(self):
        self._ihm = IhmMenu()
        self._tournement = Tournement()
        self._player = Player()

    def description_tournement(self):
        list_choix_tournement = self._ihm.menu_description_tournement()
        if list_choix_tournement[0]:
            self._tournement.name = list_choix_tournement[0]
        if list_choix_tournement[1]:
            self._tournement.location = list_choix_tournement[1]
        if list_choix_tournement[2]:
            self._tournement.date = list_choix_tournement[2]
        if list_choix_tournement[3]:
            self._tournement.time_control = list_choix_tournement[3]
        if list_choix_tournement[4]:
            self._tournement.description = list_choix_tournement[4]
        return self._tournement

    def description_player(self):
        list_players = []
        for i in range(8):
            player = Player()
            list_choix = self._ihm.menu_entrer_joueur()
            if list_choix[0]:
                self._player.first_name = list_choix[0]
            if list_choix[1]:
                self._player.last_name = list_choix[1]
            if list_choix[2]:
                self._player.date_of_birth = list_choix[2]
            if list_choix[3]:
                self._player.sex = list_choix[3]
            if list_choix[4]:
                self._player.ranking = list_choix[4]
            if list_choix[5]:
                self._player.id_player = list_choix[5]
            list_players.append(player)
        return list_players

    def report_first_part(self):
        boole = True
        db = TinyDB('db.json')
        players_table = db.table('players')
        tournement_table = db.table('tournement')
        while boole:
            self._ihm.menu_rapport()
            choice_menu_report = self._ihm.saisie_int(" Choisissez une action : --> ")
            if choice_menu_report == 1:
                list_players = sorted(players_table.all(), key=itemgetter('first_name'))
                for player in list_players:
                    self._ihm.print_string(player)
            if choice_menu_report == 2:
                list_players = sorted(players_table.all(), key=itemgetter('ranking'), reverse=True)
                for player in list_players:
                    self._ihm.print_string(player)
            if choice_menu_report == 3:
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    self._ihm.print_string("Tournement " + tournois[i]['name_tournement'] + ":")
                    list_players = sorted(tournois[i]['list_player'], key=itemgetter('first_name'))
                    for player in list_players:
                        self._ihm.print_string(player)
            if choice_menu_report == 4:
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    self._ihm.print_string("Tournement " + tournois[i]['name_tournement'] + ":")
                    list_players = sorted(tournois[i]['list_player'], key=itemgetter('ranking'), reverse=True)
                    for player in list_players:
                        self._ihm.print_string(player)
            if choice_menu_report == 5:
                boole = False

    def report_second_part(self):
        boole = True
        while boole:
            self._ihm.menu_rapport_2()
            db = TinyDB('db.json')
            tournement_table = db.table('tournement')
            choice_menu_report = self._ihm.saisie_int(" Choisissez une action : --> ")
            if choice_menu_report == 6:
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    self._ihm.print_string(
                        tournois[i]['name_tournement'] + "," + tournois[i]['location'] + "," + tournois[i]['date'] +
                        str(tournois[i]['nb_round']) + "," + tournois[i]['time_control'] + "," +
                        tournois[i]['description'])
            if choice_menu_report == 7:
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    self._ihm.print_string("Tournement " + tournois[i]['name_tournement'] + ":")
                    list_rounds = tournois[i]['list_round']
                    for round in list_rounds:
                        self._ihm.print_string(round)
            if choice_menu_report == 8:
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    self._ihm.print_string("Tournement " + tournois[i]['name_tournement'] + ":")
                    list_match = tournois[i]['list_match']
                    for match in list_match:
                        self._ihm.print_string(match)
            if choice_menu_report == 9:
                boole = False
