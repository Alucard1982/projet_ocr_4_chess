from modele.joueur import Player
from modele.tournement_progress import Round
from modele.tournement_progress import Match
import datetime


class ControleurTournementProgress:

    def __init__(self):
        self._gestion_match = Match()

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

    def pair_players_round1(self):
        list_players = self.create_players()
        round1 = Round("round", str(datetime.datetime.now()))
        round1.first_round(list_players)
        return round1

    def scored_match_round1(self, round1):
        self._gestion_match.list_match = round1.list_match
        list_scored_player = self._gestion_match.score_match()
        round1.end_date = str(datetime.datetime.now())
        return list_scored_player

    def pair_player_round2(self):
        round2 = Round("round2", str(datetime.datetime.now()))
        round2.list_match = self._gestion_match.list_end_round
        round2.next_round()
        return round2

    def scored_match_round2(self, round2):
        self._gestion_match.list_match = round2.list_match
        list_scored_player = self._gestion_match.score_match()
        round2.end_date = str(datetime.datetime.now())
        return list_scored_player

    def pair_player_round3(self):
        round3 = Round("round3", str(datetime.datetime.now()))
        round3.list_match = self._gestion_match.list_end_round
        round3.next_round()
        return round3

    def scored_match_round3(self, round3):
        self._gestion_match.list_match = round3.list_match
        list_scored_player = self._gestion_match.score_match()
        round3.end_date = str(datetime.datetime.now())
        return list_scored_player

    def pair_player_round4(self):
        round4 = Round("round4", str(datetime.datetime.now()))
        round4.list_match = self._gestion_match.list_end_round
        round4.next_round()
        return round4

    def scored_match_round4(self, round4):
        self._gestion_match.list_match = round4.list_match
        list_scored_player = self._gestion_match.score_match()
        round4.end_date = str(datetime.datetime.now())
        return list_scored_player
