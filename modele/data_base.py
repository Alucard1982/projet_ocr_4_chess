from modele.joueur import Player
from modele.tournement_progress import Round
from tinydb import TinyDB


class DataTiny:

    def __init__(self):
        pass

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

    def truncate(self):
        db = TinyDB('db.json')
        match_table = db.table('match_rank')
        round_table = db.table('round')
        match_paired_table = db.table('match_paired')
        match_table.truncate()
        round_table.truncate()
        match_paired_table.truncate()

    def insert_player_and_tournement(self, list_players, tournois):
        db = TinyDB('db.json')
        all_players_table = db.table('all_players')
        player_by_tournement = db.table('player_by_tournement')
        player_by_tournement.truncate()
        tournement_description = db.table('tournement')
        for player in list_players:
            tournois.add_player(player)
            player_dic = player.to_dict()
            if player_dic not in all_players_table:
                all_players_table.insert(player_dic)
            player_by_tournement.insert(player_dic)
        tournement_description.insert({'name_tournement': tournois.name, 'location': tournois.location,
                                       'date': tournois.date, 'nb_round': tournois.nb_round,
                                       'time_control': tournois.time_control,
                                       'description': tournois.description})

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

    def pull_data(self):
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
        list_data = [list_rounds, list_rank_player]
        return list_data
