from operator import itemgetter


class Round:
    def __init__(self, name="", star_date=None, end_date=None):
        self._list_match = []
        self._list_match_paired = []
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
    def list_match_paired(self):
        return self._list_match_paired

    @list_match_paired.setter
    def list_match_paired(self, value):
        self._list_match_paired = value

    @property
    def name(self):
        return self._name

    @name.setter
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

    def __repr__(self):
        return " {} {} {}".format(self._name, self._star_date, self._end_date)

    def first_round(self, list_players):
        list_player_sorted = (sorted(list_players, key=lambda player: player.ranking, reverse=True))
        list_players_strong = list_player_sorted[:4]
        list_players_weak = list_player_sorted[-4:]
        self._list_match.append(([list_players_strong[0]], [list_players_weak[0]]))
        self._list_match.append(([list_players_strong[1]], [list_players_weak[1]]))
        self._list_match.append(([list_players_strong[2]], [list_players_weak[2]]))
        self._list_match.append(([list_players_strong[3]], [list_players_weak[3]]))
        return self._list_match

    def next_round(self):
        while len(self._list_match) != 0:
            i = 1
            while self._list_match[0][0].id_player in self._list_match[i][0].tag_player:
                i = i + 1
            self._list_match_paired.append((self._list_match[0], self._list_match[i]))
            self._list_match.remove(self._list_match[i])
            self._list_match.remove(self._list_match[0])


class Match(Round):
    def __init__(self):
        self._list_end_round = []

    @property
    def list_end_round(self):
        return self._list_end_round

    @property
    def list_match(self):
        return self._list_match

    @list_match.setter
    def list_match(self, value):
        self._list_match = value

    def _saisie_int(self, message):
        try:
            return float(input(message))
        except ValueError:
            print("attention ce n'est pas un nombre compris entre 0 et 1")
            return self._saisie_int(message)

    def score_match(self):
        list_scored_player = []
        i = 0
        for player1_score, player2_score in self._list_match:
            i = i + 1
            choix_joueur1 = self._saisie_int("Rentrer le score du du joueur1 du match" + str(i) + "\n")
            choix_joueur2 = self._saisie_int("Rentrer le score du joueur2 du match" + str(i) + "\n")
            if len(player1_score) == 1:
                player1_score.append(choix_joueur1)
                player2_score.append(choix_joueur2)
            else:
                player1_score[1] += choix_joueur1
                player2_score[1] += choix_joueur2
            player1_score[0].add_oppenent(player2_score[0].id_player)
            player2_score[0].add_oppenent(player1_score[0].id_player)
            list_scored_player.append(player1_score)
            list_scored_player.append(player2_score)

        list_scored_player_sorted = (sorted(list_scored_player, key=lambda player: player[0].ranking, reverse=True))
        self._list_end_round = (sorted(list_scored_player_sorted, key=itemgetter(1), reverse=True))
        return self._list_end_round
