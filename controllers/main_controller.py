from views.main_view import MainView
from ddb.main_models import MainModel
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
        self.main_model = MainModel()
        self.view = MainView()


    def main_menu(self):
        pass

    def start(self):
        pass