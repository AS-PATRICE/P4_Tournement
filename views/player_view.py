from models.players import Player
from controllers.player_controller import PlayerController



class PlayerView:
    """

    """
    def __init__(self):
        # self.Player = Player()
        # self.PlayerController = PlayerController()
        pass

    def choice_menu_player(self):
        print("~~~~~ Menu manage player ~~~~~~~")
        print("Create player ................ 1")
        print("show all players list......... 2")
        print("Search players ............... 3")
        print("Update players ............... 4")
        print("Return to the main menu....... R")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        choice = input("Your choice to manage player: ")
        return choice


