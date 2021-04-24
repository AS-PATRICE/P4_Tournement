from .tournament import Tournament

class Round:
    """
    """

    def __init__(self, start_date, end_date, round_name=(), player_list=[],  game_list=[]):
        self.round_name = () # Tuple_name = ("R1", "R2", "R3", "R4")
        self.start_date = start_date
        self.end_date = end_date
        self.player_list = []
        self.game_list = []




