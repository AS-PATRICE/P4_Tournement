from .players import Player
from .tournament import Tournament
from .round import Round
from .game import Game
from .paring import Paring


class MainModel:
    """

    """

    def __init__(self):
        self.Tournament = Tournament()
        self.Player = Player()
        self.Round = Round()
        self.Game = Game()
        self.Paring = Paring()
