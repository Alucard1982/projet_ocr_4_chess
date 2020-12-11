from modele.joueur import Player
from modele.tournement_progress import Match
from modele.tournement_progress import Round
from modele.tournois import Tournement
from modele.data_base import DataTiny
from controleur.controleur_menu import ControleurMenu
from vue.view import IhmMenu

import datetime


class ControleurTournementProgress:

    def __init__(self):
        """
        Constructeur de la classe ControleurTournementProgress
        Permet d'utiliser les attributs à l'instanciation de la classe ControleurTournementProgress
        """
        self._gestion_match = Match()
        self._gestion_tournement = Tournement()
        self._ihm = IhmMenu
        self._controleur_meu = ControleurMenu()
        self._data_tiny = DataTiny()

    def create_players(self):
        """
        Méthode de la classe ControleurTournementProgress
        permet la création d'objets Player automatique
        :return: une liste d'objet Player
        """
        player1 = Player("aojo1", "dubois", "14mai", "male", 1800, 1)
        player2 = Player("bojo2", "dubois", "14mai", "male", 1400, 2)
        player3 = Player("cojo3", "dubois", "14mai", "male", 1500, 3)
        player4 = Player("dojo4", "dubois", "14mai", "male", 1600, 4)
        player5 = Player("eojo5", "dubois", "14mai", "male", 1700, 5)
        player6 = Player("fojo6", "dubois", "14mai", "male", 1850, 6)
        player7 = Player("gojo7", "dubois", "14mai", "male", 1550, 7)
        player8 = Player("hojo8", "dubois", "14mai", "male", 1450, 8)

        list_players = [player1, player2, player3, player4, player5, player6, player7, player8]
        return list_players


    def round1(self, list_players):
        """
        Méthode de la classe ControleurTournementProgress
        Permet le deroulement du permier round du tournois suisse
        :param:liste de player
        :return: l'objet round qui est le premier round du tournois
        """
        round1 = Round("round1", str(datetime.datetime.now()))
        match_paired = round1.first_round(list_players)
        self._ihm.print_string(round1.list_match)
        round1.list_match_paired = match_paired
        self._gestion_match.list_match = round1.list_match
        self._ihm.print_string(self._gestion_match.score_match(match_paired))
        round1.end_date = str(datetime.datetime.now())
        return round1

    def more_round(self, round1):
        """
        Méthode de la classe ControleurTournementProgress
        Permet le déroulement de chaque round jusqu à la fin du tournois
        excepté pour le round 1
        On peut arreter le tournois en cours
        :param round1:
        :return: La liste de tous les objets rounds du tournois
        """
        list_rounds = [round1]
        for i in range(self._gestion_tournement.nb_round - 1):
            self._ihm.print_string("*******************ROUND NEXT******************\n")
            round = Round("round" + str(i + 2), str(datetime.datetime.now()))
            round.list_match = self._gestion_match.list_end_round
            match_paired = round.next_round()
            self._ihm.between_round()
            self._data_tiny.insert_report(list_rounds)
            choice_between_round = self._ihm.saisie_int_next_round(" Choisissez une action : --> ")
            if choice_between_round == 1:
                self._ihm.print_string(round.list_match_paired)
                self._ihm.print_string(self._gestion_match.score_match(match_paired))
                round.end_date = str(datetime.datetime.now())
                list_rounds.append(round)
                self._data_tiny.insert_report(list_rounds)
            if choice_between_round == 2:
                self._data_tiny.push_between_round(list_rounds, round)
                break
            if choice_between_round == 3:
                self._data_tiny.push_between_round(list_rounds, round)
                self._controleur_meu.report_first_part()
                self._controleur_meu.report_second_part()
                break

    def resume_tournement(self):

        list_data = self._data_tiny.pull_data()
        list_rounds, list_rank_player = list_data
        nb_real_round = self._gestion_tournement.nb_round - (len(list_rounds))
        self._ihm.print_string("************** Il reste " + str(nb_real_round) +
                               " rounds avant la fin du tournois************")
        self._ihm.print_string(list_rank_player)
        for i in range(nb_real_round):
            self._ihm.print_string("*******************ROUND NEXT******************\n")
            round = Round("round_next", str(datetime.datetime.now()))
            if i == 0:
                round.list_match = list_rank_player
            else:
                round.list_match = self._gestion_match.list_end_round
            macth_paired = round.next_round()
            self._ihm.between_round()
            choice_between_round = self._ihm.saisie_int_next_round(" Choisissez une action : --> ")
            self._ihm.print_string(round.list_match_paired)
            if choice_between_round == 1:
                self._ihm.print_string(self._gestion_match.score_match(macth_paired))
                round.end_date = str(datetime.datetime.now())
                list_rounds.append(round)
                self._data_tiny.insert_report(list_rounds)
            if choice_between_round == 2:
                self._data_tiny.push_between_round(list_rounds, round)
                break
            if choice_between_round == 3:
                self._data_tiny.push_between_round(list_rounds, round)
                self._controleur_meu.report_first_part()
                self._controleur_meu.report_second_part()
                break
            if i == nb_real_round:
                self._data_tiny.truncate()
