from models.game import Game
from models.round import Round


class RoundController:
    """

    """
    def __init__(self):
        self.game = Game()
        self.round = Round()

    def __unicode__(self):
        return ([(self.game.player), "+ ", (self.game.player_score)], ": ", [(self.game.opponent), "+ ", (self.game.opponent_score)])



