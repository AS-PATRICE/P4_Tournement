from .main_models import MainModel

class Tournament:
    """
    Gestion de la création des tournois
    Cette classe doit permettre la sauvegarde des enregistrement des joueurs dans la base-de-donnée players
    """

    def __init__(self, tour_name, place, start_date, end_date, description, time_control=None, number_of_player=8, player_list=[], round_list=[], results=[]):
        self.tour_name = tour_name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = None
        self.number_of_player = 8
        self.player_list = []
        self.round_list = []
        self.results = []

    # def __init__(self, tour_name, place, start_date, end_date, description, **kwargs):
    #     self.id = None
    #     self.num = None
    #     self.tour_name = tour_name
    #     self.place = place
    #     self.start_date = start_date
    #     self.end_date = end_date
    #     self.time_control = None
    #     self.description = description
    #     self.players = []
    #     self.round = []
    #     if kwargs:
    #         for attr_key, attr_value in kwargs.items():
    #             setattr(self, attr_key, attr_value)


    def serialize_tournament(self):
        serialized_tournament = {
            "tour_name": self.tour_name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "time_control": self.time_control,
            "description": self.description,
            "number_of_player": self.number_of_player,
            "player_list": self.player_list,
            "round_list": self.round_list,
            "results": self.results
        }
        return serialized_tournament


