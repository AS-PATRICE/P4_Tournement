from tinydb import TinyDB, where
from models.tournament import Tournament


class TournamentController:
    """

    """
    def __init__(self):
        pass


    @staticmethod
    def save_tournament(tournament):
        db = TinyDB("./ddb/db.json")
        tournaments_table = db.table("tournaments")
        results = tournaments_table.search(where("tour_name") == tournament.tour_name)
        print(results)
        if len(results) == 0:
            tournament.serialize_tournament()
            tournaments_table.insert(tournament.serialize_tournament())
        else:
            print("the tournament has been registered successfully")


    def create_tournament(self):
        tour_name = (input("Tournament name : "))
        place = (input("place: "))
        start_date = (input("start date : "))
        end_date = (input("End date : "))
        time_control = (input("Time Control: "))
        description = (input("Description: "))
        tournament = Tournament(tour_name, place, start_date, end_date, description)
        TournamentController.save_tournament(tournament)

    def show_all_tournament_list(self):
        db = TinyDB("ddb/db.json")
        tournaments_table = db.table("tournaments")
        results = tournaments_table .all()

        for tournament in results:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("tour_name:", tournament["tour_name"])
            print("place:", tournament["place"])
            print("start_date:", tournament["start_date"])
            print("end_date:", tournament["end_date"])
            print("time_control:", tournament["time_control"])
            print("description:", tournament["description"])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

