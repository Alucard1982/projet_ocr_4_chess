from controleur.controleur import ControleurTournementProgress
from vue.view import IhmMenu
from modele.joueur import Player
from controleur.controleur_menu import ControleurMenu
from tinydb import TinyDB


def lol():
    player1 = {"nom": "jojo", "prenom": "jaja"}
    player2 = {"nom": "jojo2", "prenom": "jaja2"}
    list_player = [player1, player2]
    db = TinyDB('db.json')
    players_table = db.table('players')
    for player in players_table.all():
        print(player.values())

def test():
    db = TinyDB('db.json')
    players_table = db.table('players')
    for player in players_table.all():
        print(player.values())


if __name__ == '__main__':

    controleur = ControleurMenu()
    controleur.tournement_software()
    """round1 = controleur.pair_players_round1()
        list_scored_player = controleur.scored_match_round1(round1)
        print(list_scored_player)

        round2 = controleur.pair_player_round2(list_scored_player)
        list_scored_player_round2 = controleur.scored_match_round2(round2)
        print(list_scored_player_round2)

        round3 = controleur.pair_player_round3(list_scored_player_round2)
        list_scored_player_round3 = controleur.scored_match_round3(round3)
        print(list_scored_player_round3)

        round4 = controleur.pair_player_round4(list_scored_player_round3)
        final_ranking = controleur.scored_match_round3(round4)
        print(final_ranking)"""




    """def tournement_software(self):
        tournois = self.description_tournement()
        # list_players = self.description_player
        controleur = ControleurTournementProgress()
        list_players = controleur.create_players()
        db = TinyDB('db.json')
        players_table = db.table('players')
        for player in list_players:
            tournois.add_player(player)
            players_table.insert({'first_name': player.first_name, 'last_name': player.last_name,
                                  'date_of_birth': player.date_of_birth, 'sex': player.sex,
                                  'ranking': player.ranking})
        IhmMenu.menu_generale()
        choice_menu_generale = int(input(" Choisissez une action : --> "))
        if choice_menu_generale == 1:
            list_rounds = self.chess_tournement()
            for rounde in list_rounds:
                tournois.add_round(rounde)
            tournement_table = db.table('tournement')
            tournement_table.insert({'name': tournois.name, 'location': tournois.location, 'date': tournois.date,
                                     'nb_round': tournois.nb_round, 'round': tournois.list_round,
                                     'players': tournois.list_players, 'time_control': tournois.time_control,
                                     'description': tournois.description})
        if choice_menu_generale == 2:
            pass
        if choice_menu_generale == 3:
            print("BYEEEEEEEEEEEEEEEEE")"""
