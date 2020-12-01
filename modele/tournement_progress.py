from operator import itemgetter, attrgetter


class Round:
    def __init__(self, name="", star_date="", end_date=""):
        self._list_match = []
        self._name = name
        self._star_date = star_date
        self._end_date = end_date

    @property
    def list_match(self):
        return self._list_match

    @list_match.setter
    def list_match(self, value):
        self._list_match = value

    @property
    def name(self):
        return self._name

    @list_match.setter
    def name(self, value):
        self._name = value

    @property
    def star_date(self):
        return self._star_date

    @star_date.setter
    def star_date(self, value):
        self._star_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    def first_round(self, list_players):
        list_player_sorted = (sorted(list_players, key=lambda player: player.ranking, reverse=True))
        list_players_strong = list_player_sorted[:4]
        list_players_weak = list_player_sorted[-4:]
        self._list_match.append(([list_players_strong[0]], [list_players_weak[0]]))
        self._list_match.append(([list_players_strong[1]], [list_players_weak[1]]))
        self._list_match.append(([list_players_strong[2]], [list_players_weak[2]]))
        self._list_match.append(([list_players_strong[3]], [list_players_weak[3]]))

    def next_round(self, list_scored_player):
        list_score_1 = []
        list_score_0 = []
        list_score_draw = []
        list_scored_player_sorted = (sorted(list_scored_player, key=itemgetter(1), reverse=True))

        lol = (sorted(list_scored_player_sorted, key=itemgetter(0), reverse=True))
        print(lol)



class Match:

    @staticmethod
    def saisie_int(message):
        try:
            return int(input(message))
        except ValueError:
            print("attention ce n'est pas un nombre compris entre 0 et 1")
            return Match.saisie_int(message)

    @staticmethod
    def score_match(list_match):
        list_scored_player = []
        i = 0
        for player1, player2 in list_match:
            i = i + 1
            choix_joueur1 = Match.saisie_int("rentrer le score du joueur1 du match" + str(i) + "\n")
            choix_joueur2 = Match.saisie_int("rentrer le score du joueur2 du match" + str(i) + "\n")
            player1.append(choix_joueur1)
            player2.append(choix_joueur2)
            list_scored_player.append(player1)
            list_scored_player.append(player2)

        return list_scored_player
