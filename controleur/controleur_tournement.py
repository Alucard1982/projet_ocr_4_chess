from modele.joueur import Player
from modele.tournement_progress import Round
from modele.tournement_progress import Match
from modele.tournois import Tournement
from vue.view import IhmMenu
from tinydb import TinyDB
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
        round1 = Round("round1", str(datetime.datetime.now()))
        match_paired = round1.first_round(list_players)
        self._ihm.print_string(round1.list_match)
        round1.list_match_paired = match_paired
        self._gestion_match.list_match = round1.list_match
        self._ihm.print_string(self._gestion_match.score_match())
        round1.end_date = str(datetime.datetime.now())
        return round1

    def more_round(self, round1):
        list_rounds = [round1]
        for i in range(self._gestion_tournement.nb_round - 1):
            self._ihm.print_string("*******************ROUND NEXT******************\n")
            round = Round("round" + str(i), str(datetime.datetime.now()))
            round.list_match = self._gestion_match.list_end_round
            round.next_round()
            self._ihm.print_string(round.list_match_paired)
            self._gestion_match.list_match = round.list_match_paired
            self._ihm.print_string(self._gestion_match.score_match())
            round.end_date = str(datetime.datetime.now())
            list_rounds.append(round)
        return list_rounds

    def to_object_player(self, dic):
        player = Player(dic['first_name'], dic['last_name'], dic['date_of_birth'], dic['sex'],
                        dic['ranking'], dic['id_player'])
        return player

    def to_object_round(self, dic):
        round = Round(dic['name'], dic['start_date'], dic['end_date'])
        return round

    def push_tinydb(self, list_rounds, round):
        list_dic_player_rank = []
        list_dic_round = []
        db = TinyDB('db.json')
        match_table = db.table('match_rank')
        round_table = db.table('round')
        for player_rank_score in round.list_player_scored:
            dic_player_match = player_rank_score[0].to_dict()
            dic_player_rank = {"player1": dic_player_match, "score_player1": player_rank_score[1]}
            list_dic_player_rank.append(dic_player_rank)
        match_table.insert({"player_scored": list_dic_player_rank})
        for rounde in list_rounds:
            dic_round = {'name': rounde.name, "start_date": rounde.star_date,
                         "end_date": rounde.end_date}
            list_dic_round.append(dic_round)
        round_table.insert({'nb_round': list_dic_round})

    def more_round_test(self, round1):
        list_rounds = [round1]
        for i in range(self._gestion_tournement.nb_round - 1):
            self._ihm.print_string("*******************ROUND NEXT******************\n")
            round = Round("round" + str(i), str(datetime.datetime.now()))
            round.list_match = self._gestion_match.list_end_round
            round.next_round()
            self._ihm.between_round()
            choice_between_round = self._ihm.saisie_int_nextround(" Choisissez une action : --> ")
            if choice_between_round == 1:
                self._ihm.print_string(round.list_match_paired)
                self._gestion_match.list_match = round.list_match_paired
                self._ihm.print_string(self._gestion_match.score_match())
                round.end_date = str(datetime.datetime.now())
                list_rounds.append(round)
            if choice_between_round == 2:
                self.push_tinydb(list_rounds, round)
                break
        return list_rounds

    def resume_tournement(self):

        list_rank_player = []
        list_rounds = []
        db = TinyDB('db.json')
        match_table = db.table('match_rank')
        round_table = db.table('round')
        dic_player_rank = match_table.all()
        dic_player_score = dic_player_rank[0]['player_scored']
        for elem in dic_player_score:
            list_rank_player.append([self.to_object_player(elem['player1']), elem["score_player1"]])
        dic_round = round_table.all()
        dic_round_description = dic_round[0]['nb_round']
        for elem in dic_round_description:
            list_rounds.append(self.to_object_round(elem))
        nb_real_round = self._gestion_tournement.nb_round - (len(list_rounds))
        self._ihm.print_string("************** Il reste " + str(nb_real_round) +
                               " rounds avant la fin du tournois************")
        self._ihm.print_string(list_rank_player)
        for i in range(nb_real_round):
            self._ihm.print_string("*******************ROUND NEXT******************\n")
            round = Round("round" + str(i), str(datetime.datetime.now()))
            if i == 0:
                round.list_match = list_rank_player
            else:
                round.list_match = self._gestion_match.list_end_round
            round.next_round()
            self._ihm.between_round()
            choice_between_round = self._ihm.saisie_int_nextround(" Choisissez une action : --> ")
            self._ihm.print_string(round.list_match_paired)
            if choice_between_round == 1:
                self._gestion_match.list_match = round.list_match_paired
                self._ihm.print_string(self._gestion_match.score_match())
                round.end_date = str(datetime.datetime.now())
                list_rounds.append(round)
            if choice_between_round == 2:
                self.push_tinydb(list_rounds, round)
                break
        return list_rounds
