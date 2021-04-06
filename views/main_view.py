from .player_view import PlayerView
from .tournament_view import TournamentView
from .report_view import ReportView


class MainView:
    """

    """
    def __init__(self):
        self.PlayerVieuw = PlayerView()
        self.TournamentVieuw = TournamentView()
        self.ReportView = ReportView()
