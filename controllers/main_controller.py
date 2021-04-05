from .player_controller import PlayerController
from .tournament_controller import TournamentController
from .report_controller import ReportController

class MainController:
    """

    """
    def __init__(self):
        self.tournament = TournamentController()
        self.player = PlayerController()
        self.report = ReportController()

    def start(self):
        self.tournament.create_tournament()