from .player_view import PlayerView
from .tournament_view import TournamentView
from .report_view import ReportView


class MainView:
    """

    """
    def __init__(self):
        self.playerView = PlayerView()
        self.tournamentView = TournamentView()
        self.reportView = ReportView()


    def main_menu(self):
        """Doit servire de menu principal. """
        print("~~~~~~~~~~~~ Main menu ~~~~~~~~~~~~~")
        print("[1] Manage tournament ............ 2")
        print("[2] Manage player ................ 1")
        print("[3] Manage reports ............... 3")
        print("[4] Clean board .................. 4")
        print("[L] leave the programme............L")
        choice = input("Your choice : ")
        print("")
        return choice

    def tournament_choice_menu(self):
        print("~~~~~ Tournament management menu ~~~~~~~~~~")
        print("Create tournament ....................... 1")
        print("Add player for tournament................ 2")
        print("Add games score ......................... 3")
        print("search tournament ....................... 4")
        print("Update tournament ....................... 5")
        print("Delate tournament ....................... 6")
        print("Show all players tournament list......... 7")
        print("Show all tournament list................. 8")
        print("Return to the main menu.................. R")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #tournament_choice_menu = input("Your choice to manage tournament: ")
        print("")
        #return tournament_choice_menu

    def player_choice_menu(self):
        print("~~~~~ Player management menu ~~~~~~~")
        print("Create player .................... 1")
        print("show all players list............. 2")
        print("Search players ................... 3")
        print("Update players ................... 4")
        print("Return to the main menu........... R")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #player_choice_menu = input("Your choice to manage player: ")
        print("")
        #return player_choice_menu

    def report_choice_menu(self):
        print("~~~~~ Report management menu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("List of actors in alphabetical order .................... 1")
        print("List of actors in order of ranking ...................... 2")
        print("List of tournament players in alphabetical order ........ 3")
        print("List of players in a tournament in order of ranking ..... 4")
        print("List of all tournaments ................................. 5")
        print("List of all rounds in a tournament ...................... 6")
        print("List of tournament matches .............................. 7")
        print("Return to the main menu ................................. R")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #report_choice_menu = input("Your choice to manage player: ")
        print("")
        #return report_choice_menu
