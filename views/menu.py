""" Define menu"""


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
    def run_main_menu():
        choice = View.main_menu()
        while choice != 1 and choice != 2 and choice != 3:
            print("Veuillez saisir un numéro existant.")
            choice = input("Veuillez entrer le numéro de l'action voulue : ")
            choice = int(choice)
        if choice == 1:
            View.create_tournament()
        elif choice == 2:
            View.create_round()
        elif choice == 3:
            View.finish_roud()

    @staticmethod
    def create_tournament():
        print("Crétion du Tournoi")
        pass

    @staticmethod
    def create_round():
        print("test2")

    @staticmethod
    def finish_roud():
        print("test3")
