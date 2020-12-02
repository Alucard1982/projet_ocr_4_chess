from modele.joueur import Player
from modele.tournement_progress import Round
from modele.tournement_progress import Match


class ControleurTournementProgress:

    def __init__(self):
        pass

    def create_players(self):
        player1 = Player("jojo1", "dubois", "14mai", "male", 1800, 1)
        player2 = Player("jojo2", "dubois", "14mai", "male", 1400, 2)
        player3 = Player("jojo3", "dubois", "14mai", "male", 1500, 3)
        player4 = Player("jojo4", "dubois", "14mai", "male", 1600, 4)
        player5 = Player("jojo5", "dubois", "14mai", "male", 1700, 5)
        player6 = Player("jojo6", "dubois", "14mai", "male", 1850, 6)
        player7 = Player("jojo7", "dubois", "14mai", "male", 1550, 7)
        player8 = Player("jojo8", "dubois", "14mai", "male", 1450, 8)

        list_players = [player1, player2, player3, player4, player5, player6, player7, player8]
        return list_players

    def pair_players_round1(self):
        round1 = Round()
        list_players = self.create_players()
        round1.first_round(list_players)
        return round1

    def scored_match_round1(self, round1):
        list_scored_player = Match.score_match(round1.list_match)
        return list_scored_player

    def pair_player_round2(self, list_player_scored):
        round2 = Round()
        round2.next_round(list_player_scored)
        return round2

    def scored_match_round2(self, round2):
        list_scored_player = Match.score_match(round2.list_match)
        return list_scored_player

    def pair_player_round3(self, list_player_scored):
        round3 = Round()
        round3.next_round(list_player_scored)
        return round3

    def scored_match_round3(self, round3):
        list_scored_player = Match.score_match(round3.list_match)
        return list_scored_player

    def pair_player_round4(self, list_player_scored):
        round4 = Round()
        round4.next_round(list_player_scored)
        return round4

    def scored_match_round4(self, round4):
        Match.score_match(round4.list_match)
