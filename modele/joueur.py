class Player:

    def __init__(self, first_name="", last_name="", date_of_birth="",
                 sex="", ranking=None, id_player=None):
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._sex = sex
        self._ranking = ranking
        self._id_player = id_player
        self._tag_player = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value

    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def ranking(self, value):
        if value < 0:
            raise ValueError("Sorry, no numbers ranking below zero")
        self._ranking = value

    @property
    def id_player(self):
        return self._id_player

    @id_player.setter
    def id_player(self, value):
        self._id_player = value

    @property
    def tag_player(self):
        return self._tag_player

    def add_oppenent(self, player):
        self._tag_player.append(player)

    def __repr__(self):
        return " {} {} {} {} {}".format(self._first_name,
                                        self._last_name,
                                        self._ranking,
                                        self._id_player,
                                        self._tag_player, )

    def to_dict(self):
        diction = {"first_name": self._first_name,
                   "last_name": self._last_name,
                   "date_of_birth": self._date_of_birth,
                   "sex": self._sex,
                   "ranking": self._ranking,
                   "tag_player": self._tag_player,
                   "id_player": self._id_player}
        return diction
