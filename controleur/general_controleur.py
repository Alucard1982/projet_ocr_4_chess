from controleur.controleur_menu import ControleurMenu
from controleur.controleur_tournement import ControleurTournementProgress
from modele.data_base import DataTiny
from vue.view import IhmMenu


class ControleurGenerale:
    def __init__(self):
        self._menu = ControleurMenu()
        self._tournement_progress = ControleurTournementProgress()
        self._ihm = IhmMenu()
        self._data_tiny = DataTiny()

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
                tournois = self._menu.description_tournement()
                # choix entre joueurs automatiques ou joueurs rentrés à la main
                list_players = self._tournement_progress.create_players()
                # list_players = self._menu.description_player()
                self._data_tiny.insert_player_and_tournement(list_players, tournois)
                self._chess_tournement(list_players)
            if choice_menu_generale == 2:
                self._tournement_progress.resume_tournement()
            if choice_menu_generale == 3:
                self._menu.report_first_part()
                self._menu.report_second_part()
            if choice_menu_generale == 4:
                boole = False
                self._ihm.print_string("THX FOR PLAYING CHESS!! HAVE A NICE DAY")
