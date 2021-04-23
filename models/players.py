
class Player:
    """

    """



    def __init__(self, last_name, first_name, birth_date, gender, score=None, ranking=None, tournament_points= 0.0, tournament_list=[], opponents=[]):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.score = None
        self.ranking = None
        self.tournament_points = 0.0
        self.tournament_list = [None]
        self.opponents = []


    # def __init__(self, **kwargs):
    #     self.id = None
    #     self.tour_name = None
    #     self.place = None
    #     self.start_date = None
    #     self.end_date = None
    #     self.time_control = None
    #     self.description = None
    #     self.players = []
    #     self.round = []
    #     if kwargs:
    #         for attr_key, attr_value in kwargs.items():
    #             setattr(self, attr_key, attr_value)


    def serialize_player(self):
        serialized_player = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "score": self.score,
            "ranking": self.ranking,
            "tournament_points": self.tournament_points,
            "tournament_list": self.tournament_list,
            "opponents": self.opponents,

        }
        return serialized_player
