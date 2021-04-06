from models.main_models import Player
from tinydb import TinyDB, where, Query

class DataBase:
    """

    """
    def __init__(self):
        self.Player = Player

    def serializes_player(self, player):
        serialized_player = {
            "last_name": player.l_name,
            "first_name": player.f_name,
            "born": player.born,
            "gender": player.gender,
            "score": player.score,
            "base_Ranking": player.baseRanking,
            "ranking": player.gender
        }

        db = TinyDB("ddb/db.json")
        players_table = db.table("players")
        players_table.insert(serialized_player)

    last_name = (input("Player last name : "))
    first_name = (input("Player first name : "))
    born = (input("Player birth date : "))
    gender = (input("Player gender : "))

    player = Player(last_name, first_name, born, gender)

    serializes_player(player)