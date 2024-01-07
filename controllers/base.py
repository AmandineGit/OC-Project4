""" Define main controllers."""
from models.tournament import Tournament
from models.player import Player
from views.menu import View
from models.file_json import JsonFile



class Controllers:
    """Classe principale """
    @staticmethod
    def main_menu():
        """Gestion des sous menu"""
        View.display_main_menu()
        choice = View.prompt_main_menu()
        while choice != 1 and choice != 2 and choice != 3 and choice != 5 and choice != 6:
            View.display_error_menu()
            choice = View.prompt_main_menu()
            choice = int(choice)
        if choice == 1:
            Controllers.create_tournament()
        elif choice == 2:
            Controllers.open_tournament()
        elif choice == 3:
            Controllers.create_players()
        elif choice == 5:
            View.prompt_lauch_round()
        elif choice == 6:
            View.prompt_finish_roud()

    @staticmethod
    def create_tournament():
        """Création d'un tournoi"""
        name, location = View.prompt_create_tournament()
        Tournament.record_tournament(name, location)
        View.display_create_tournament(name)
        Controllers.main_menu()

    @staticmethod
    def open_tournament():
        """Démarre un tournoi"""
        datas_open_tournament = View.prompt_open_tournament()
        if datas_open_tournament == "x":
            Controllers.main_menu()
        else:
            if Tournament.current_tournament() is not None:
                View.display_error_tournamentinprogress()
            else:
                open_date = str(datas_open_tournament[1])
                tournament_name = (datas_open_tournament[0])
                if Tournament.search_tournament(tournament_name) is True:
                    json_tournament = JsonFile("tournaments.json", [])
                    tournaments = JsonFile.read_json(json_tournament)
                    for tournament in tournaments:
                        if tournament.get("name") == datas_open_tournament[0]:
                            tournament["start_date"] = datas_open_tournament[1]
                            Tournament.update_tournament(tournament)
                            View.display_open_tournament(tournament_name, open_date)
                            Controllers.create_players()
                else :
                    View.display_error_tournament(tournament_name)
        Controllers.main_menu()

    @staticmethod
    def create_players():
        """Création et enregistrement sur un tournoi de users"""
        tournament_exist = False
        while tournament_exist is False:
            lauch = View.prompt_create_players()
            if lauch != "n" and lauch != "y":
                View.display_error_choisecreateuser()
            elif lauch == "n":
                Controllers.main_menu()
            elif lauch == "y":
                datas = View.prompt_datas_player()
                first_name, last_name, date_of_birth, tournament_name = datas
                tournament_exist = Tournament.search_tournament(tournament_name)
                if tournament_exist is False:
                    View.display_error_tournament(tournament_name)
        while datas is not None:
            datas_player = first_name, last_name, date_of_birth
            player_exist = Player.search_player(datas_player)
            if player_exist is True:
                 Controllers.registrer_player_tournament(datas)
            else:
                player = Player(first_name, last_name, date_of_birth)
                dataswip = datas
                Player.record_player(player, "players.json")
                Controllers.registrer_player_tournament(dataswip)
            datas = View.prompt_create_players()
        Controllers.main_menu()

    def registrer_player_tournament(self):
        """Ajouter un player dans un tournoi
        Rechercher le tournoi en cours
        Ajouter le player dans la liste de players du tournoi grace à la methode update_tournament"""
        json_tournament = JsonFile("tournaments.json", [])
        tournaments = JsonFile.read_json(json_tournament)
        for tournament in tournaments:
            if tournament.get("name") == self[3]:
                players_list = tournament["registred_players_list"]
                players_list.append([self[0], self[1]])
                tournament["registred_players_list"] = players_list
                for tournamentnew in tournaments:
                    if tournamentnew.get("name") == tournament["name"]:
                        tournamentnew["registred_players_list"] = tournament["registred_players_list"]
                        Tournament.update_tournament(tournamentnew)
                View.display_register_player(self[0], self[1], self[3])

    @staticmethod
    def lauch_round():
        """Lancer un round"""
