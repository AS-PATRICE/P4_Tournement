

class Game:
    """
    Cette classe correspond à un match, une rencontre opposant deux joueurs.
    """
    playerScores = ((0, 0), (0.5, 0.5), (1, 1))


    def __init__(self, player, playerScore, playerOpponent, playerOpponentScore, roundName, startTime, endTime, tourName):
        self.player = player  # the player
        self.playerScore = ((0, 0), (0.5, 0.5), (1, 1))  # The score can be choices in playerScores: 1.0 pt for the winner, opt for loser or 0.5 if null
        self.playerOpponent = playerOpponent  # the player and opponent
        self.playerOpponentScore = playerOpponentScore  # The score can be choices in playerScores: 1.0 pt for the winner, opt for loser or 0.5 if null
        self.roundName = roundName  # The nomber of round R1, R2, R3, R4
        self.startTime = startTime
        self.endTime = endTime
        self.tourName = tourName
