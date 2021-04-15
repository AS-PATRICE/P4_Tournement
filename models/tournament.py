
class Tournament:
    """
    Gestion de la création des tournois
    Cette classe doit permettre la sauvegarde des enregistrement des joueurs dans la base-de-donnée players
    """

    def __init__(self, tour_name, place, start_date, end_date, time_control, description, players = 0, round = 0):
        self.tour_name = tour_name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.description = description
        self.players = 0
        self.round = 0


    def serialize_tournament(self):
        serialized_tournament = {
            "tour_name": self.tour_name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "time_control": self.time_control,
            "description": self.description,
            "players": self.players,
            "round": self.round
        }
        return serialized_tournament


