from models.players import Player
from tinydb import TinyDB, where, Query



class PlayerController:
    """

    """
    def __init__(self):
        pass


    @staticmethod
    def save_player(player):
        db = TinyDB("../ddb/db.json")
        players_table = db.table("players")
        results = players_table.search(where("last_name") == player.last_name and where("first_name") == player.first_name)

        if len(results) == 0:
            print(player.serialize_player())
            #players_table.insert({"last_name": last_name, "first_name": first_name, "born": born, "gender": gender})
            players_table.insert(player.serialize_player())
        else:
            print("the player has been registered successfully")

    def show_all_player(self):
        db = TinyDB("ddb/db.json")
        players_table = db.table("players")
        results = players_table.all()

        for player in results:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("last_name:", player["last_name"])
            print("first_name:", player["first_name"])
            print("born:", player["born"])
            print("gender:", player["gender"])
            print("ranking:", player["ranking"])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def search_player(self, last_name, first_name):
        db = TinyDB("ddb/db.json")
        players_table = db.table("players")
        results = players_table.search(where("last_name") == last_name and where("first_name") == first_name)
        for player in results:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("last_name:", player["last_name"])
            print("first_name:", player["first_name"])
            print("born:", player["born"])
            print("gender:", player["gender"])
            print("ranking:", player["ranking"])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

