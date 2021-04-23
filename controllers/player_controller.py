from models.players import Player
from tinydb import TinyDB, where
#from .main_controller import MainController



class PlayerController:
    """

    """
    def __init__(self):
        pass

    @staticmethod
    def save_player(player):
        db = TinyDB("./ddb/db.json")
        players_table = db.table("players")
        results = players_table.search(where("last_name") == player.last_name and where("first_name") == player.first_name)
        print(results)
        if len(results) == 0:
            player.serialize_player()
            players_table.insert(player.serialize_player())

        else:
            print("the player  has been registered successfully")


    def create_player(self):
        last_name = (input("Player last name : "))
        first_name = (input("Player first name : "))
        birth_date = (input("Player birth date : "))
        gender = (input("Player gender : "))
        player = Player(last_name, first_name, birth_date, gender)
        PlayerController.save_player(player)


    def show_all_player(self):
        db = TinyDB("ddb/db.json")
        players_table = db.table("players")
        results = players_table.all()

        for player in results:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("last_name:", player["last_name"])
            print("first_name:", player["first_name"])
            print("birth_date:", player["birth_date"])
            print("gender:", player["gender"])
            #print("ranking:", player["ranking"])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def search_player(self, last_name, first_name):
        db = TinyDB("ddb/db.json")
        players_table = db.table("players")
        results = players_table.search(where("last_name") == last_name and where("first_name") == first_name)
        for player in results:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("last_name:", player["last_name"])
            print("first_name:", player["first_name"])
            print("birth_date:", player["birth_date"])
            print("gender:", player["gender"])
            print("ranking:", player["ranking"])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

