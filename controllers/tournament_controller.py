from tinydb import TinyDB, where
from models.tournament import Tournament

class TournamentController:
    """

    """
    def __init__(self):
        pass

    def manage_menu_player(self):
        choice_p = "x"
        while choice_p != "q" and choice_p != "Q":
            print()
            choice_p = input("Your choice to manage player : ")
            if choice_p == "1":
                # inscription des joueurs dans la base de donnée
                print("Appel du controleur playersManagement")
            elif choice_p == "2":
                # création d'un nouveau tournoi
                print("Importation du controleur tournementManager")
            elif choice_p == "3":
                # Ajout de 8 joueurs qui prendront part au tournois
                print("Entrer les résultats des matchs")
            elif choice_p == "4":
                # Gestion des rapports
                print("Importation du controleur reportManager")
            else:
                print("Retour au programme principal.")
            print()


    @staticmethod
    def save_tournament(tournament):
        db = TinyDB("./ddb/db.json")
        tournaments_table = db.table("tournaments")
        results = tournaments_table.search(where("tour_name") == tournament.tour_name)
        if len(results) == 0:
            print(tournament.serialize_tournament())
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
        tournament = Tournament(tour_name, place, start_date, end_date, time_control, description)
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

