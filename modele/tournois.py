class Tournement:

    def __init__(self, name, location, date, description):
        self._name = name
        self._location = location
        self._date = date
        self._nb_round = 4
        self._list_round = []
        self._list_players = []
        self._time_control = ["blitz", "bullet", "quick hit"]
        self._description = description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def nb_round(self):
        return self._nb_round

    @nb_round.setter
    def nb_round(self, value):
        self._nb_round = value

    @property
    def list_round(self):
        return self._list_round

    @list_round.setter
    def list_round(self, value):
        self._list_round = value

    @property
    def list_players(self):
        return self._list_players

    @list_players.setter
    def list_players(self, value):
        self._list_players = value

    @property
    def time_control(self):
        return self._time_control

    @time_control.setter
    def time_control(self, value):
        self._time_control = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
