""" Define menu"""
import sys
sys.path.append("/home/mandine/PycharmProjects/OC-Project4/")
from controllers.base import Controllers

class View:
    """Vue du menu principal"""

    @staticmethod
    def main_menu():
        """Prompt pour sélectionner un sous menu"""
        print("Gestion des tournois")
        print("")
        print("1. Créer un tournoi")
        print("2. Créer un round")
        print("3. Marquer un round comme terminé.")
        print("")
        main_menu_number = input("Veuillez entrer le numéro de l'action voulue : ")
        main_menu_number = int(main_menu_number)
        return main_menu_number

    @staticmethod
    def prompt_main_menu():
        choice = View.main_menu()
        while choice != 1 and choice != 2 and choice != 3:
            print("Veuillez saisir un numéro existant.")
            choice = input("Veuillez entrer le numéro de l'action voulue : ")
            choice = int(choice)
        if choice == 1:
            View.prompt_create_tournament()
        elif choice == 2:
            View.prompt_create_round()
        elif choice == 3:
            View.prompt_finish_roud()

    @staticmethod
    def prompt_create_tournament():
        print("Création du Tournoi")
        tournament_location = input("Veuillez indiquer le lieu du tournoi : ")
        tournament_name = input("Veuillez indiquer le nom du tournoi : ")
        Controllers.create_tournament(tournament_name, tournament_location)
        print("Le tournoi '" + tournament_name + "' est enregistré")

    @staticmethod
    def prompt_create_round():
        print("test2")

    @staticmethod
    def prompt_finish_roud():
        print("test3")
