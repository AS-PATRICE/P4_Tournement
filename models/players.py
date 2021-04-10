
class Player:
    """

    """



    def __init__(self, last_name, first_name, born, gender, score=0, baseRanking=0, ranking=0):
        self.last_name = last_name
        self.first_name = first_name
        self.born = born
        self.gender = gender
        self.score = 0
        self.baseRanking = 0
        self.ranking = 0



    def serialize_player(self):
        serialized_player = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "born": self.born,
            "gender": self.gender,
            "score": self.score,
            "base_Ranking": self.baseRanking,
            "ranking": self.ranking
        }
        return serialized_player
