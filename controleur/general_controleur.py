from controleur.controleur_tournement import ControleurTournementProgress
from controleur.controleur_menu import ControleurMenu
from vue.view import IhmMenu
from tinydb import TinyDB


class ControleurGenerale:
    def __init__(self):
        self._menu = ControleurMenu()
        self._tournement_progress = ControleurTournementProgress()
        self._ihm = IhmMenu()

    def _chess_tournement(self):
        """
        Méthode de l'objet ControleurGenerale qui fait le déroulement du tournois suisse
        retrun: la liste de tous les rounds du tournois
        """
        self._ihm.print_string("*******************ROUND1******************\n")
        round1 = self._tournement_progress.round1()
        list_rounds = self._tournement_progress.more_round_test(round1)
        return list_rounds

    def _insert_report(self, list_players, tournois, list_rounds):
        """
        Méthode l'objet ControleurGenerale qui permet de mettre les données de tout le tournois dans tinyDB
        :param list_players: list de player
        :param tournois: l'objet tournois
        :param list_rounds:  liste des rounds
        """
        db = TinyDB('db.json')
        players_table = db.table('players')
        list_dic_player = []
        list_dic_round = []
        list_dic_match = []
        for player in list_players:
            tournois.add_player(player)
            player_dic = player.to_dict()
            players_table.insert(player_dic)
            list_dic_player.append(player_dic)
        for rounde in list_rounds:
            tournois.add_round(rounde)
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
        tournement_table.insert({'name_tournement': tournois.name, 'location': tournois.location,
                                 'date': tournois.date, 'nb_round': tournois.nb_round,
                                 'time_control': tournois.time_control, 'description': tournois.description,
                                 'list_player': list_dic_player, 'list_round': list_dic_round,
                                 'list_match': list_dic_match})

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
                # list_players = self._menu.description_player
                list_players = self._tournement_progress.create_players()
                list_rounds = self._chess_tournement()
                if len(list_rounds) == 4:
                    self._insert_report(list_players, tournois, list_rounds)

            if choice_menu_generale == 2:
                list_rounds = self._tournement_progress.resume_tournement()
                self._insert_report(list_players, tournois, list_rounds)
            if choice_menu_generale == 3:
                self._menu.report_first_part()
                self._menu.report_second_part()
            if choice_menu_generale == 4:
                boole = False
                self._ihm.print_string("THX FOR PLAYING CHESS!! HAVE A NICE DAY")
