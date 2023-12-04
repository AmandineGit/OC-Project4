""" Define main controllers."""
from models.tournament import Tournament
from models.player import Player
from views.menu import View
from models.file_json import JsonFile


class Controllers:
    """Classe principale """
    @staticmethod
    def main_menu():
        """Prompt pour sélectionner un sous menu"""
        choice = View.display_main_menu()
        while choice != 1 and choice != 2 and choice != 5 and choice != 6:
            print("Veuillez saisir un numéro existant.")
            choice = input("Veuillez entrer le numéro de l'action voulue : ")
            choice = int(choice)
        if choice == 1:
            Controllers.create_tournament()
        elif choice == 2:
            Controllers.create_players()
        elif choice == 5:
            View.prompt_lauch_round()
        elif choice == 6:
            View.prompt_finish_roud()

    @staticmethod
    def create_tournament():
        name, location = View.prompt_create_tournament()
        Tournament.record_tournament(name, location)
        View.display_create_tournament(name)
        datas = View.prompt_create_players()

    def create_players():
        datas = View.prompt_create_players()
        while datas is not None:
            first_name, last_name, date_of_birth = datas
            player_exist = Player.search_player(datas)
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
        Ajouter le player dans la liste de players du tournoi grace à la methode updat_tournament"""

        json_tournament = JsonFile("tournaments.json", [])
        tournaments = JsonFile.read_json(json_tournament)
        for tournament in tournaments:
            if tournament.get("end_date") == "01/01/2000"\
                    and tournament.get("start_date") != "01/01/2000":
                players_list = tournament["registred_players_list"]
                players_list.append([self[0], self[1]])
                tournament["registred_players_list"] = players_list
                for tournamentnew in tournaments:
                    if tournamentnew.get("name") == tournament["name"]:
                        tournamentnew["registred_players_list"] = tournament["registred_players_list"]
                        Tournament.update_tournament(tournamentnew)
                View.display_register_player(self[0], self[1])
