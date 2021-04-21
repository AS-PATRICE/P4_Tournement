from tinydb import TinyDB


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