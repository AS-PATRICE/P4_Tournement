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

        choice = True
        while choice != "r" and choice != "R":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Create player ................ 1")
            print("show all players list......... 2")
            print("Search players ............... 3")
            print("Update players ............... 4")
            print("Return to the main menu....... R")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


            choice = input("Your choice : ")

            if choice == "1":

               PlayerController.create_player(self)

            elif choice == "2":
                PlayerController.show_all_player(self)

            elif choice == "3":
                last_name = str(input("Player last name : "))
                first_name = str(input("Player first name : "))
                PlayerController.search_player(last_name, first_name)


            else:
                choice = False

# if __name__ == '__main__':
#     joueur = PlayerView()
#     joueur.choice_menu_player()