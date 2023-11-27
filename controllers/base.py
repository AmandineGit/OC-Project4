""" Define main controllers."""
import json
from models.tournament import Tournament
from models.player import Player
from views.menu import View


class Controllers:
    """Classe principale """
    @staticmethod
    def main_menu():
        """Prompt pour sélectionner un sous menu"""
        choice = View.main_menu()
        while choice != 1 and choice != 2 and choice != 5 and choice != 6:
            print("Veuillez saisir un numéro existant.")
            choice = input("Veuillez entrer le numéro de l'action voulue : ")
            choice = int(choice)
        if choice == 1:
            Controllers.create_tournament()
        elif choice == 2:
            Controllers.create_player()
        elif choice == 5:
            View.prompt_lauch_round()
        elif choice == 6:
            View.prompt_finish_roud()

    @staticmethod
    def create_tournament():
        name, location = View.prompt_create_tournament()
        tournament = Tournament(name, location)
        try:
            with open("tournament.json", "a") as f:
                json.dump(tournament.__dict__, f)
                f.write("\n")
        except Exception:
            print("Erreur lors de l'enregistrement du fichier tournament.json .")
        View.display_create_tournament(name)
        Controllers.create_player()

    @staticmethod
    def create_player():
        datas = View.prompt_create_players()
        while datas is not None:
            datas = Player.record_player(datas)
        Controllers.main_menu()
