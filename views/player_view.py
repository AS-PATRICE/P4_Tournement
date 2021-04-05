from models.players import Player
from controllers.player_controller import PlayerController


player = Player(last_name=["last_name"], first_name=["first_name"], born=["born"], gender=["gender"])


class PlayerView:
    """

    """
    def __init__(self):
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
            # gestion du choix
            if choice == "1":
                last_name = (input("Player last name : "))
                first_name = (input("Player first name : "))
                born = (input("Player birth date : "))
                gender = (input("Player gender : "))
                player.save_player(last_name, first_name, born, gender)

            elif choice == "2":
                player.show_all_player()

            elif choice == "3":
                last_name = str(input("Player last name : "))
                first_name = str(input("Player first name : "))
                player.search_player_by_first_name(last_name, first_name)

            elif choice == "4":
                print("Update player")
            else:
                choice = False
                print("Return to the main menu")
