

class Game:
    """
    Cette classe correspond à un match, une rencontre opposant deux joueurs.
    """
    results = ((0, 0), (0.5, 0.5), (1, 1))


    def __init__(self, player, opponent, start_time, end_time, round_name, tour_name, player_score= 0.0, opponent_score= 0.0):
        self.player = player
        self.opponent = opponent
        self.start_time = start_time
        self.end_time = end_time
        self.round_name = round_name  # The number of round R1, R2, R3, R4
        self.tour_name = tour_name
        self.player_score = 0.0
        self.opponent_score = 0.0

