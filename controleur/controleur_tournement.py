from modele.joueur import Player
from modele.tournement_progress import Round
from modele.tournement_progress import Match
from modele.tournois import Tournement

from controleur.controleur_menu import ControleurMenu

from tinydb import TinyDB
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

    def to_object_player(self, dic):
        """
        Méthode de la classe ControleurTournementProgress
        Transforme un dictionnaire Player en objet Player
        :param dic: dictionnaire de Player
        :return:un objet player
        """
        player = Player(dic['first_name'], dic['last_name'], dic['date_of_birth'],
                        dic['sex'], dic['ranking'], dic['id_player'])
        player.tag_player = dic['tag_player']
        return player

    def to_object_round(self, dic):
        """
        Méthode de la classe ControleurTournementProgress
        Transforme un dictionnaire Round en objet Round
        :param dic: dictionnaire Round
        :return: un objet Round
        """
        round = Round(dic['name'], dic['start_date'], dic['end_date'])
        return round

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
            self.insert_report(list_rounds)
            choice_between_round = self._ihm.saisie_int_next_round(" Choisissez une action : --> ")
            if choice_between_round == 1:
                self._ihm.print_string(round.list_match_paired)
                self._ihm.print_string(self._gestion_match.score_match(match_paired))
                round.end_date = str(datetime.datetime.now())
                list_rounds.append(round)
                self.insert_report(list_rounds)
            if choice_between_round == 2:
                self.push_between_round(list_rounds, round)
                break
            if choice_between_round == 3:
                self.push_between_round(list_rounds, round)
                self._controleur_meu.report_first_part()
                self._controleur_meu.report_second_part()
                break

    def resume_tournement(self):
        """
        Méthode de la classe ControleurTournementProgress
        Permet de reprendre le tournois à l'état ou on l'a quitter et de finir le tournois
        Ici on récupere les données dans TinyDb pour la suite du tournois
        :return: la lists de tous les objets rounds du tournois
        """
        list_rank_player = []
        list_rounds = []
        list_match_paird = []
        db = TinyDB('db.json')
        match_table = db.table('match_rank')
        round_table = db.table('round')
        match_paired_table = db.table('match_paired')
        dic_player_rank = match_table.all()
        try:
            dic_player_score = dic_player_rank[0]['player_scored']
        except IndexError:
            print("IL N Y A PAS DE TOURNOIS EN COURS!!!!!")
        for elem in dic_player_score:
            list_rank_player.append([self.to_object_player(elem['player1']), elem["score_player1"]])
        dic_round = round_table.all()
        dic_round_description = dic_round[0]['round']
        for elem in dic_round_description:
            roundes = self.to_object_round(elem)
            list_rounds.append(roundes)
        dic_match = match_paired_table.all()
        dic_match_paired = dic_match[0]['list_match_paired']
        for match in dic_match_paired:
            list_match_paird.append(([self.to_object_player(match['player1']),
                                      match['score_player1']],
                                     [self.to_object_player(match['player2']),
                                      match['score_player2']]))
        list_rounds[-1].list_match_paired = list_match_paird
        match_table.truncate()
        round_table.truncate()
        match_paired_table.truncate()
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
                self.insert_report(list_rounds)
            if choice_between_round == 2:
                self.push_between_round(list_rounds, round)
                break
            if choice_between_round == 3:
                self.push_between_round(list_rounds, round)
                self._controleur_meu.report_first_part()
                self._controleur_meu.report_second_part()
                break
            if i == nb_real_round:
                match_table.truncate()
                round_table.truncate()
                match_paired_table.truncate()

    def insert_report(self, list_rounds):
        """
        Méthode l'objet ControleurGenerale qui permet de mettre les données du tournois dans tinyDB
        :param list_rounds:  liste des rounds
        """
        list_dic_round = []
        list_dic_match = []
        db = TinyDB('db.json')
        players_by_tournement = db.table('player_by_tournement')
        list_dic_player = players_by_tournement.all()
        for rounde in list_rounds:
            dic_round = {'name_round': rounde.name, "start_date": rounde.star_date,
                         "end_date": rounde.end_date}
            list_dic_round.append(dic_round)
            for match in rounde.list_match_paired:
                dic_player1_match = match[0][0].to_dict()
                dic_player2_match = match[1][0].to_dict()
                dic_match = {"player1": dic_player1_match, "score_player1": match[0][1],
                             "player2": dic_player2_match, "score_player2": match[1][1]}
                list_dic_match.append(dic_match)
        tournement_table = db.table('tournement')
        tournois = tournement_table.all()
        id_tournement = len(tournois)
        tournement_table.update({'list_player': list_dic_player, 'list_round': list_dic_round,
                                 'list_match': list_dic_match}, doc_ids=[id_tournement])

    def push_between_round(self, list_rounds, round):
        """
        Méthode de la classe ControleurTournementProgress
        Permet de rentrer les données des player avec leur scores ainsi que les rounds dans tinyDb
        :param list_rounds: list de tout les round joué
        :param round: le dernier round joué
        """
        list_dic_player_rank = []
        list_dic_round = []
        list_dic_match = []
        db = TinyDB('db.json')
        match_table = db.table('match_rank')
        round_table = db.table('round')
        match_paired_table = db.table('match_paired')
        for player_rank_score in round.list_player_scored:
            dic_player_match = player_rank_score[0].to_dict()
            dic_player_rank = {"player1": dic_player_match, "score_player1": player_rank_score[1]}
            list_dic_player_rank.append(dic_player_rank)
        match_table.insert({"player_scored": list_dic_player_rank})
        for rounde in list_rounds:
            dic_round = {'name': rounde.name, "start_date": rounde.star_date,
                         "end_date": rounde.end_date}
            list_dic_round.append(dic_round)
            for match in rounde.list_match_paired:
                dic_player1_match = match[0][0].to_dict()
                dic_player2_match = match[1][0].to_dict()
                dic_match = {"player1": dic_player1_match, "score_player1": match[0][1],
                             "player2": dic_player2_match, "score_player2": match[1][1]}
                list_dic_match.append(dic_match)
        round_table.insert({'round': list_dic_round})
        match_paired_table.insert({'list_match_paired': list_dic_match})
