class Tournament:
    """
    Gestion de la création des tournois
    Cette classe doit permettre la sauvegarde des enregistrement des joueurs dans la base-de-donnée players
    """
    number_of_tournament = 0
    def __init__(self, tourName, place, startDate, endDate, round, players, timeControl, description, tourNomber=4):
        self.tourName = tourName
        self.place = place
        self.startDate = startDate
        self.endDate = endDate
        self.round = []
        self.players = players
        self.timeControl = timeControl
        self.description = description

        Tournament.number_of_tournament +=1