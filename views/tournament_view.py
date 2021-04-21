from models.tournament import Tournament
from controllers.tournament_controller import TournamentController


class TournamentView:
    def __init__(self):
        pass

    def create_tournament(self):
        tour_name = (input("Tournament name : "))
        place = (input("place: "))
        start_date = (input("start date : "))
        end_date = (input("End date : "))
        time_control = (input("Time Control: "))
        description = (input("Description: "))
        tournament = Tournament(tour_name, place, start_date, end_date, time_control, description)
        TournamentController.save_tournament(tournament)

    def choice_menu_tournament(self):

        choice = True
        while choice != "r" and choice != "R":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("** Create tournament ................ 1")
            print("** Add players....................... 2")
            print("** Add games scores.................. 2")
            print("** show all tournament list.......... 2")
            print("** Search one tournament ............ 3")
            print("** Update one tournament ............ 4")
            print("** Return to the main menu........... R")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            choice = input("Your choice : ")

            if choice == "1":

                TournamentView.create_tournament(self)

            elif choice == "2":
                #TournamentController.show_all_tournament()
                pass

            elif choice == "3":
                #tour_name = str(input("Player last name : "))
                #TournamentController.search_tournament(tour_name)
                pass


            else:
                choice = False




# if __name__ == '__main__':
#     tournois = TournamentView()
#     tournois.create_tournament()