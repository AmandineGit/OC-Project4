""" Define menu"""


class View:
    """Vue du menu principal"""

    @staticmethod
    def display_main_menu():
        """Affichage du menu principal et  prompt pour sélectionner un sous menu"""
        print("Gestion des tournois\n")
        print("1. Créer un tournoi")
        print("2. Inscrire des joueurs à un tournoi")
        print("3. Lancer un tournoi")
        print("4. Cloturer un tournoi")
        print("5. Lancer un round")
        print("6. Cloturer un round")
        print("7. Afficher un rapport\n")
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
        print("\n===> Le tournoi '" + self + "' est enregistré")

    @staticmethod
    def prompt_create_players():
        """Prompt pour créer un player ou plusieurs"""
        lauch = input("\nVoulez vous enregistrer un nouveau joueur ? y/n ")
        if lauch != "n" and lauch != "y":
            lauch = input("\nMerci de répondre par y pour yes ou n pour no\n"
                          "Voulez vous enregistrer un nouveau joueur ? y/n ")
        while lauch == "y":
            print("\nEnregistrement des joueurs")
            first_name = input("\nVeuillez indiquer le prénom du joueur : ")
            last_name = input("Veuillez indiquer le nom du joueur : ")
            date_of_birth = input("Veuillez indiquer la date de naissance du joueur sous le format jj/mm/yy : ")
            return first_name, last_name, date_of_birth
        else:
            return None

    def display_create_player(self, last_name):
        print("\n===> Le joueur " + self + " " + last_name + " est inscrit")

    @staticmethod
    def prompt_lauch_round():
        print("test2")

    @staticmethod
    def prompt_finish_roud():
        print("test3")
