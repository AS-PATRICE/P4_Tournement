

class Round:
    """
    """
    roundNomber = {"R1", "R2", "R3", "R4"}
    roundGames = ["Game"]
    def __init__(self, roundGames, roundName, roundPlayers, starDate, endDate, tourName):
        self.roundGames = ["Game"]
        self.roundName = {"R1", "R2", "R3", "R4"}
        self.roundPlayers = roundPlayers
        self.starDate = starDate
        self.endDate = endDate
        self.tourName = tourName


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
