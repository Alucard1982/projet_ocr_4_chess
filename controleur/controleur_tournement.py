from modele.joueur import Player
from modele.tournement_progress import Round
from modele.tournement_progress import Match
from modele.tournois import Tournement
from vue.view import IhmMenu
import datetime


class ControleurTournementProgress:

    def __init__(self):
        self._gestion_match = Match()
        self._gestion_tournement = Tournement()
        self._ihm = IhmMenu

    def create_players(self):
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

    def round1(self):
        list_players = self.create_players()
        round1 = Round("round0", str(datetime.datetime.now()))
        match_paired = round1.first_round(list_players)
        self._ihm.print_string(round1.list_match)
        round1.list_match_paired = match_paired
        self._gestion_match.list_match = round1.list_match
        self._ihm.print_string(self._gestion_match.score_match())
        round1.end_date = str(datetime.datetime.now())
        return round1

    def more_round(self, round1):
        list_round = [round1]
        for i in range(self._gestion_tournement.nb_round - 1):
            self._ihm.print_string("*******************ROUND NEXT******************\n")
            round = Round("round" + str(i), str(datetime.datetime.now()))
            round.list_match = self._gestion_match.list_end_round
            round.next_round()
            self._ihm.print_string(round.list_match_paired)
            self._gestion_match.list_match = round.list_match_paired
            self._ihm.print_string(self._gestion_match.score_match())
            round.end_date = str(datetime.datetime.now())
            list_round.append(round)
        return list_round

