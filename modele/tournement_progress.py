from operator import itemgetter


class Round:
    """
              Une classe utilisé pour réprésenter un round

              ...

              Attributs
              ----------
               name : str
                  le nom du round
               star_date : date
                  la date du debut du tournoi
               end_date : date
                  la date de fin de tournoi
               list_match:list
                permet de récuperer la list des players trier par score et ranking à la fin du round
                list_match_paired:list
                   list des matchs(1 match = 2 joueurs)
               list_player_score:list
                   list des joueur classé par score et ranking

              Methods
              -------
              __repr__()
                  Permet d'afficher l'objet round
              first_round()
                  Permet le pairage du round 1 qui est spécifique
              next_round()
                  Permet le pairage de tout les rounds jusqu'a la fin du tournoi
              """

    def __init__(self, name="", star_date=None, end_date=None):

        """Constructeur de la classe Round qui va permettre de créer l'objet round"""

        self._list_match = []
        self._list_match_paired = []
        self._list_player_scored = []
        self._name = name
        self._star_date = star_date
        self._end_date = end_date

    """ getteur et setteur"""

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
    def list_player_scored(self):
        return self._list_player_scored

    @list_player_scored.setter
    def list_player_scored(self, value):
        self._list_player_scored = value

    def add_player_scored(self, player):
        self._list_player_scored.append(player)

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
        """

        Méthode de la classe Round
        Permet l'affichage de l'objet Round
        :return: les attributs de l'objet qu'on veut afficher
        """
        return " {} {} {}".format(self._name, self._star_date, self._end_date)

    def first_round(self, list_players):
        """

        Méthode de la classe Round
        Permet de trier une list de joueur en fonction du classement au 1 round
        d'un tournois suisse .
        Créer des Paires de joueurs pour chaque match, toujours en fonction du systeme suisse
        pour le 1er round.
        :param list_players: la list des joueur du tournois
        :return: une list de match.Un match equivaux à deux joueurs
        """
        list_player_sorted = (sorted(list_players, key=lambda player: player.ranking, reverse=True))
        list_players_strong = list_player_sorted[:4]
        list_players_weak = list_player_sorted[-4:]
        self._list_match.append(([list_players_strong[0]], [list_players_weak[0]]))
        self._list_match.append(([list_players_strong[1]], [list_players_weak[1]]))
        self._list_match.append(([list_players_strong[2]], [list_players_weak[2]]))
        self._list_match.append(([list_players_strong[3]], [list_players_weak[3]]))
        return self._list_match

    def next_round(self):
        """

        Méthode de la classe Round
        Permet de pairer les joueurs par match en fonction du système suisse .
        Un joueur ne peux pas rejouer contre un autre joueur.
        Cette méthode s'applique pour tout les rounds du tournois excepter le round 1.
        :return:la liste des matchs avec le pairage de chaque joueur
        """
        for elem in self._list_match:
            self._list_player_scored.append(elem)
        """while len(self._list_match) != 0:
            i = 1
            while self._list_match[0][0].id_player in self._list_match[i][0].tag_player:
                i = i + 1
            self._list_match_paired.append((self._list_match[0], self._list_match[i]))
            del self._list_match[i]
            del self._list_match[0]
        return self._list_match_paired"""

        nb_players = len(self._list_match)
        for i in range(0, nb_players, 2):
            j = i + 1
            while j < nb_players and self._list_match[i][0].id_player in self._list_match[j][0].tag_player:
                j = j + 1
            if j == nb_players:
                j = i - 1
                while not self.echange_possible(i + 1, j):
                    j = j - 1
            var_temporaire = self._list_match[j]
            self._list_match[j] = self._list_match[i + 1]
            self._list_match[i + 1] = var_temporaire
        for i in range(0, nb_players, 2):
            self._list_match_paired.append((self._list_match[i], self._list_match[i + 1]))
        return self._list_match_paired

    def echange_possible(self, i, j):
        echange_possible = True
        if i % 2 == 0:
            adversaire_i = i + 1
        else:
            adversaire_i = i - 1
        if j % 2 == 0:
            adversaire_j = j + 1
        else:
            adversaire_j = j - 1
        if self._list_match[i][0].id_player in self._list_match[adversaire_j][0].tag_player:
            echange_possible = False
        if self._list_match[j][0].id_player in self._list_match[adversaire_i][0].tag_player:
            echange_possible = False
        return echange_possible


class Match:
    """
             Une classe utilisé pour réprésenter un match

             ...

             Attributs
             ----------
              list_end_round : list
                list des players avec le score classé par score et ranking à la fin du round

             Methods
             -------

             saisie_int()
                permet de sécuriser les saisies des scores
             score_match()
                 Permet d'appliquer un score à chaque joueur
             """
    def __init__(self):

        """Constructeur de la classe Match qui va permettre de créer l'objet match"""

        self._list_end_round = []

    """getteur et setteur"""
    @property
    def list_end_round(self):
        return self._list_end_round

    def _saisie_int(self, message):
        try:
            return float(input(message))
        except ValueError:
            print("attention ce n'est pas un nombre compris entre 0 et 1")
            return self._saisie_int(message)

    def score_match(self, match_paired):
        """

        Méthode de la classe Match
        Permet d'appliquer un score à chaque joueur de chaque match.
        Elle va aussi permettre de de tagger le player avec l'id_player pour pouvoir savoir si un joueur
        a deja joué contre un autre.
        :return: une list de joueur classé par point et par ranking
        """
        list_scored_player = []
        i = 0
        for player1_score, player2_score in match_paired:
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
