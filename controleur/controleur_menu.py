from vue.view import IhmMenu
from modele.joueur import Player
from modele.tournois import Tournement
from tinydb import TinyDB
from operator import itemgetter


class ControleurMenu:
    def __init__(self):
        """
        Constructeur de la classe ControleurMenu
        Permet d'utiliser les attributs à l'instenciation de la classe ControleurMenu
        """
        self._ihm = IhmMenu()
        self._tournement = Tournement()

    def description_tournement(self):
        """
        Méthode de la classe ControleurMenu
        Permet de rentrer les données du tournois
        :return:l'objet tournois
        """
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
        """
        Méthode de la classe ControleurMenu
        Permet de rentrer les données des players
        :return: une liste d'objet player
        """
        list_players = []
        for i in range(8):
            player = Player()
            list_choix = self._ihm.menu_entrer_joueur()
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
        print(list_players)
        return list_players

    def report_first_part(self):
        """
        Méthode de la classe ControleurMenu
        Première partie du rapport de fin tournois
        Choix en fonction du menu rapport
        """
        boole = True
        db = TinyDB('db.json')
        while boole:
            all_players_table = db.table('all_players')
            tournement_table = db.table('tournement')
            tournement_description = db.table('tournement_description')
            self._ihm.menu_rapport()
            choice_menu_report = self._ihm.saisie_int(" Choisissez une action : --> ")
            if choice_menu_report == 1:
                list_players = sorted(all_players_table.all(), key=itemgetter('first_name'))
                for player in list_players:
                    self._ihm.print_string(player)
            if choice_menu_report == 2:
                list_players = sorted(all_players_table.all(), key=itemgetter('ranking'), reverse=True)
                for player in list_players:
                    self._ihm.print_string(player)
            if choice_menu_report == 3:
                tournement_description = tournement_description.all()
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    self._ihm.print_string("Tournement " + tournement_description[i]['name_tournement'] + ":")
                    list_players = sorted(tournois[i]['list_player'], key=itemgetter('first_name'))
                    for player in list_players:
                        self._ihm.print_string(player)
            if choice_menu_report == 4:
                tournement_description = tournement_description.all()
                tournois = tournement_table.all()
                for i in range(len(tournois)):
                    self._ihm.print_string("Tournement " + tournement_description[i]['name_tournement'] + ":")
                    list_players = sorted(tournois[i]['list_player'], key=itemgetter('ranking'), reverse=True)
                    for player in list_players:
                        self._ihm.print_string(player)
            if choice_menu_report == 5:
                boole = False

    def report_second_part(self):
        """
        Méthode de la classe ControleurMenu
        Deuxième partie du rapport de fin de tournois
        Choix en fonction du menu rapport
        """
        boole = True
        while boole:
            self._ihm.menu_rapport_2()
            db = TinyDB('db.json')
            tournement_table = db.table('tournement')
            tournement_description = db.table('tournement_description')
            choice_menu_report = self._ihm.saisie_int(" Choisissez une action : --> ")
            if choice_menu_report == 6:
                tournement_description = tournement_description.all()
                for i in range(len(tournement_description)):
                    self._ihm.print_string(
                        tournement_description[i]['name_tournement'] + "," + tournement_description[i]['location'] +
                        "," + tournement_description[i]['date'] +
                        "," + str(tournement_description[i]['nb_round']) +
                        "," + tournement_description[i]['time_control'] +
                        "," + tournement_description[i]['description'])
            if choice_menu_report == 7:
                tournois = tournement_table.all()
                tournement_description = tournement_description.all()
                for i in range(len(tournois)):
                    self._ihm.print_string("Tournement " + tournement_description[i]['name_tournement'] + ":")
                    list_rounds = tournois[i]['list_round']
                    for round in list_rounds:
                        self._ihm.print_string(round)
            if choice_menu_report == 8:
                tournois = tournement_table.all()
                tournement_description = tournement_description.all()
                for i in range(len(tournois)):
                    self._ihm.print_string("Tournement " + tournement_description[i]['name_tournement'] + ":")
                    list_match = tournois[i]['list_match']
                    for match in list_match:
                        self._ihm.print_string(match)
            if choice_menu_report == 9:
                boole = False
