""" Define menu"""
from models.tournament import Tournament
from datetime import datetime

class View:
    """Vue du menu principal"""

    @staticmethod
    def display_main_menu():
        """Affichage du menu principal des sous menus"""
        print("Gestion des tournois\n")
        print("1. Créer un tournoi")
        print("2. Inscrire des joueurs à un tournoi")
        print("3. Ouvrir un tournoi")
        print("4. Cloturer un tournoi")
        print("5. Lancer un round")
        print("6. Cloturer un round")
        print("7. Afficher un rapport\n")

    @staticmethod
    def prompt_main_menu():
        """prompt pour sélectionner un sous menu"""
        main_menu_number = input("Veuillez entrer le numéro de l'action voulue : ")
        main_menu_number = int(main_menu_number)
        return main_menu_number

    @staticmethod
    def prompt_create_tournament():
        """Prompt pour créer un tournoi qui ensuite lance le prompt pour la création des players"""
        print("\n===> Création du Tournoi")
        tournament_location = input("\nVeuillez indiquer le lieu du tournoi : ")
        tournament_name = input("Veuillez indiquer le nom du tournoi : ")
        return tournament_name, tournament_location

    def display_create_tournament(self):
        """Affiche un message confirmant la création du tournoi"""
        print("\n===> Le tournoi '" + self + "' est enregistré")

    @staticmethod
    def prompt_open_tournament():
        """Prompt pour selectionner le tournoi et receuillir la date de début d'ouverture """
        tournament_name = input("Veuillez entrer le nom du tournoi :")
        open_date_tournament = View.test_date(input("Veuillez entrer la date de début du tournoi : "))

        datas_open_tournament = [tournament_name, open_date_tournament]
        return datas_open_tournament

    @staticmethod
    def prompt_create_players():
        """Prompt pour gérer la création d'un ou de plusieurs users"""
        lauch = input("\nVoulez vous enregistrer un nouveau joueur ? y/n "
                      "\nPour revenir au menu principal taper x.\n")
        return lauch

    @staticmethod
    def prompt_datas_player():
        print("\nEnregistrement des joueurs")
        first_name = input("\nVeuillez indiquer le prénom du joueur : ")
        last_name = input("Veuillez indiquer le nom du joueur : ")
        date_of_birth = View.test_date(input("Veuillez indiquer la date de naissance du "
                                                            "joueur sous le format jj/mm/yy : "))
        tournament_name = input("Veuillez indiquer le nom du tournoi : ")
        return first_name, last_name, date_of_birth, tournament_name

    @staticmethod
    def prompt_lauch_round():
        print("test2")

    @staticmethod
    def prompt_finish_roud():
        print("test3")

    def display_register_player(self, last_name, tournament_name):
        """Affiche un message confirmant l'inscription du player"""
        print("\n===> Le joueur " + self + " " + last_name + " est inscrit au tournoi " + tournament_name+ ".")

    def display_create_player(self, last_name):
        """Affiche un message confirmant l'inscription du player"""
        print("\n===> Le joueur " + self + " " + last_name + " est enregistré dans la base de joueurs.")

    def display_error_tournament(self):
        print("Le tournoi " + self + " n'existe pas.")

    def display_open_tournament(self, start_date):
        print('le tournoi "' + self + '" est ouvert.')

    def test_date(self):
        date_str = self
        test = False
        while test is False:
            try:
                datetime.strptime(date_str, "%d/%m/%Y")
                test = True
            except ValueError:
                print("Format de date incorrect. Veuillez réessayer.")
                date_str = input("Veuillez indiquer une date sous le format jj/mm/yy : ")
        return date_str
