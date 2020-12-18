from configparser import ConfigParser


class Tournement:
    """
       Une classe utilisé pour réprésenter un tournois

       ...

       Attributs
       ----------
        name : str
           le nom du tournoi
        location : str
           la location du tournoi
        date : str
           la date du tournoi
        nb_round:int
            le noombre de round du tournoi
        list_round:list
            list de tout les rounds du tournoi
        list_player:list
            list de tout les players du tournoi
        time control:str
            représente le type de coup du tournoi
        description:str
            représente la description du tournoi

       Methods
       -------
       __repr__
           Permet d'afficher l'objet tournoi
       """

    def __init__(self, name="", location="", date="", time_control="", description=""):
        """Constructeur de la classe Tournement qui va permettre de créer l'objet tournoi"""

        parser = ConfigParser()
        parser.read('setup.cfg')
        nb_rounds = parser.get('TOURNEMENT', 'nb_rounds')
        self._name = name
        self._location = location
        self._date = date
        self._nb_round = int(nb_rounds)
        self._list_round = []
        self._list_players = []
        self._time_control = time_control
        self._description = description

    """ getteur et setteur"""
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
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def nb_round(self):
        return self._nb_round

    @property
    def list_round(self):
        return self._list_round

    def add_round(self, rounde):
        self._list_round.append(rounde)

    @property
    def list_players(self):
        return self._list_players

    def add_player(self, player):
        self._list_players.append(player)

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

    def __repr__(self):
        """

        Méthode d'affichage de l'objet Tournement
        :return: les attributs de l'objet qu'on veut afficher
        """
        return " {} {} {} {} {} {}".format(self._name,
                                           self._location,
                                           self._date,
                                           self._nb_round,
                                           self._time_control,
                                           self._description)
