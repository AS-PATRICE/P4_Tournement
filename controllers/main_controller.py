from views.main_view import MainView
from models.main_models import MainModel
from .player_controller import PlayerController
from .tournament_controller import TournamentController
from .report_controller import ReportController
from views.player_view import PlayerView
import sys
import os

class MainController:
    """
    ==> Fait lien avec le main.py
    ==> Gestion du menu principal
    ==> Gestion des vues:  player_view, tournament_view et report_view
    """
    def __init__(self):
        self.tournament = TournamentController()
        self.player = PlayerController()
        self.report = ReportController()
        self.main_model = MainModel()
        self.view = MainView()
        self.playerView = PlayerView()


    def start(self):
        """ Point de lancement du programme """
        choice = "x"
        while choice != "l" or choice != "L":
            choice = self.view.main_menu()
            if choice == "1":
                self.manage_menu_tournament()
            elif choice == "2":
                self.manage_menu_player()
            elif choice == "3":
                self.manage_menu_report()
            elif choice == "4":
                self.clear()
            else:
                print("Good bye !)")
                break

    @classmethod
    def clear(cls):
        """Methode to clean board"""
        os.system('clear')

    def manage_menu_tournament(self):
        """ Methode to mange choice menu tournament """

        choice_p = "x"
        while choice_p != "r" and choice_p != "Q":

            self.view.tournament_choice_menu()
            choice_p = input("Your choice to manage tournament : ")

            if choice_p == "1":
                print("space reserved for the creation of a tournament")
                self.tournament.create_tournament()

            elif choice_p == "2":
                print("space reserved for adding players to a tournament")
                print("space reserved for adding players to a tournament")
                print("space reserved for adding players to a tournament")
                print("space reserved for adding players to a tournament")

            elif choice_p == "3":
                print("space reserved for adding the score of players in a tournament")
                print("space reserved for adding the score of players in a tournament")
                print("space reserved for adding the score of players in a tournament")
                print("space reserved for adding the score of players in a tournament")

            elif choice_p == "4":
                print("space reserved for tournament research")
                print("space reserved for tournament research")
                print("space reserved for tournament research")
                print("space reserved for tournament research")

            elif choice_p == "5":
                print("space reserved for updating a tournament")
                print("space reserved for updating a tournament")
                print("space reserved for updating a tournament")
                print("space reserved for updating a tournament")

            elif choice_p == "6":
                print("space reserved for the deletion of a tournament")
                print("space reserved for the deletion of a tournament")
                print("space reserved for the deletion of a tournament")
                print("space reserved for the deletion of a tournament")

            elif choice_p == "7":
                print("space reserved for the display of all the players of a tournament")
                print("space reserved for the display of all the players of a tournament")
                print("space reserved for the display of all the players of a tournament")
                print("space reserved for the display of all the players of a tournament")

            elif choice_p == "8":
                print("All tournament list")
                print("")
                self.tournament.show_all_tournament_list()

            else:
                print("Return to the main program.")
            print("")


    def manage_menu_player(self):
        """ Methode to mange choice menu player """
        choice_p = "x"
        while choice_p != "r" and choice_p != "Q":

            self.view.player_choice_menu()
            choice_p = input("Your choice to manage player : ")

            if choice_p == "1":
                print(" == > Created  player")
                print("")
                self.player.create_player()

            elif choice_p == "2":
                print("space reserved for the display of all players")
                self.player.show_all_player()

            elif choice_p == "3":
                print("space reserved for the search for information on the players")
                print("space reserved for the search for information on the players")
                print("space reserved for the search for information on the players")

            elif choice_p == "4":
                print("space reserved for player update")
                print("space reserved for player update")
                print("space reserved for player update")

            elif choice_p == "5":
                print("space reserved for the deletion of players")
                print("space reserved for the deletion of players")
                print("space reserved for the deletion of players")

            else:
                print("Return to the main program.")
                break
            print("")


    def manage_menu_report(self):
        """ Methode to mange choice menu report """
        choice_p = "x"
        while choice_p != "r" and choice_p != "Q":

            self.view.report_choice_menu()
            choice_p = input("Your choice to manage tournament : ")

            if choice_p == "1":
                print("Space to list of actors in alphabetical order")
                print("Space to list of actors in alphabetical order")
                print("Space to list of actors in alphabetical order")
                print("Space to list of actors in alphabetical order")

            elif choice_p == "2":
                print("Space to List of actors in order of ranking")
                print("Space to List of actors in order of ranking")
                print("Space to List of actors in order of ranking")
                print("Space to List of actors in order of ranking")

            elif choice_p == "3":
                print("Space to list of tournament players in alphabetical order")
                print("Space to list of tournament players in alphabetical order")
                print("Space to list of tournament players in alphabetical order")
                print("Space to list of tournament players in alphabetical order")

            elif choice_p == "4":
                print("Space to list of players in a tournament in order of ranking")
                print("Space to list of players in a tournament in order of ranking")
                print("Space to list of players in a tournament in order of ranking")
                print("Space to list of players in a tournament in order of ranking")

            elif choice_p == "4":

                print("Space to list of all tournaments ")
                print("Space to list of all tournaments ")
                print("Space to list of all tournaments ")
                print("Space to list of all tournaments ")

            elif choice_p == "4":
                print("Space to list of all rounds in a tournament")
                print("Space to list of all rounds in a tournament")
                print("Space to list of all rounds in a tournament")
                print("Space to list of all rounds in a tournament")

            elif choice_p == "4":
                print("Space to list of tournament matches ")
                print("Space to list of tournament matches ")
                print("Space to list of tournament matches ")
                print("Space to list of tournament matches ")

            else:
                print("Return to the main program.")
                break
            print("")

