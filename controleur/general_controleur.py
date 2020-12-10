from controleur.controleur_tournement import ControleurTournementProgress
from controleur.controleur_menu import ControleurMenu
from vue.view import IhmMenu
from tinydb import TinyDB


class ControleurGenerale:
    def __init__(self):
        self._menu = ControleurMenu()
        self._tournement_progress = ControleurTournementProgress()
        self._ihm = IhmMenu()

    def _chess_tournement(self, list_players):
        """
        Méthode de l'objet ControleurGenerale qui fait le déroulement du tournois suisse
        retrun: la liste de tous les rounds du tournois
        """
        self._ihm.print_string("*******************ROUND1******************\n")
        round1 = self._tournement_progress.round1(list_players)
        self._tournement_progress.more_round(round1)


    def tournement_software(self):
        """
        Méthode principale de l'objet ControleurGenerale
        qui regroupe le menu,les rapports , et le déroulement du tournois
        """
        boole = True
        while boole:
            self._ihm.menu_generale()
            choice_menu_generale = self._ihm.saisie_int(" Choisissez une action : --> ")
            if choice_menu_generale == 1:
                db = TinyDB('db.json')
                all_players_table = db.table('all_players')
                player_by_tournement = db.table('player_by_tournement')
                player_by_tournement.truncate()
                tournement_description = db.table('tournement_description')
                tournois = self._menu.description_tournement()
                list_players = self._tournement_progress.create_players()
                # list_players = self._menu.description_player()
                for player in list_players:
                    tournois.add_player(player)
                    player_dic = player.to_dict()
                    all_players_table.insert(player_dic)
                    player_by_tournement.insert(player_dic)
                tournement_description.insert({'name_tournement': tournois.name, 'location': tournois.location,
                                               'date': tournois.date, 'nb_round': tournois.nb_round,
                                               'time_control': tournois.time_control,
                                               'description': tournois.description})
                self._chess_tournement(list_players)
            if choice_menu_generale == 2:
                self._tournement_progress.resume_tournement()
            if choice_menu_generale == 3:
                self._menu.report_first_part()
                self._menu.report_second_part()
            if choice_menu_generale == 4:
                boole = False
                self._ihm.print_string("THX FOR PLAYING CHESS!! HAVE A NICE DAY")
