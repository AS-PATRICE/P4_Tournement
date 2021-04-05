from models.players import Player
from tinydb import TinyDB, where, Query



class PlayerController:
    """

    """
    def __init__(self):
        self.player = Player()

    def save_player(self, last_name, first_name, born, gender):
        db = TinyDB("ddb/db.json")
        players_table = db.table("players")
        results = players_table.search(where(last_name) == last_name and where(first_name) == first_name)
        if len(results == 0):
            players_table.insert({"last_name": last_name, "first_name": first_name, "born": born, "gender": gender})
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
        User = Query()
        db = TinyDB("ddb/db.json")
        players_table = db.table("players")
        results = players_table.search(User.last_name == last_name and User.first_name == first_name)
        for player in results:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("last_name:", player["last_name"])
            print("first_name:", player["first_name"])
            print("born:", player["born"])
            print("gender:", player["gender"])
            print("ranking:", player["ranking"])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def update_player(self, last_name, first_name, born, gender):
        User = Query()
        db = TinyDB("ddb/db.json")
        players_table = db.table("players")
        last_name = str(input("Player last name : "))
        results = players_table.search(User.(self.last_Name == self.first_name))
        for res in results:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("last_name:", res["last_name"])
            print("first_name:", res["first_name"])
            print("born:", res["born"])
            print("gender:", res["gender"])
            print("ranking:", res["ranking"])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            new_last_name = str(input("Player new last name :"))
            res["last_Name"] = new_last_name
            new_first_name = str(input("Player new first name :"))
            res["first_Name"] = new_first_name
            new_born = str(input("Player new born :"))
            res["born"] = new_born
            new_gender = str(input("Player new gender :"))
            res["gender"] = new_gender
        players_table.write_back(results)

