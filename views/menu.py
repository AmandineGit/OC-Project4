""" Define menu"""
from models.tournament import Tournament
from datetime import datetime


class View:
    """Vue du menu principal"""

    @staticmethod
    def display_main_menu():
        """Affichage du menu principal"""
        print("Gestion des tournois\n")
        print("1. Créer un tournoi")
        print("2. Ouvrir un tournoi")
        print("3. Inscrire des joueurs à un tournoi")
        print("4. Lancer un round")
        print("5. Cloturer un round")
        print("6. Afficher un rapport\n")

    @staticmethod
    def prompt_menu():
        """prompt pour sélectionner un sous menu"""
        menu_number = input("Veuillez entrer le numéro de l'action voulue : ")
        return menu_number

    @staticmethod
    def prompt_create_tournament():
        """Prompt pour créer un tournoi qui ensuite lance le prompt pour la création des players"""
        print("\n===> Création du Tournoi")
        tournament_location = input("\nVeuillez indiquer le lieu du tournoi : ")
        tournament_name = input("Veuillez indiquer le nom du tournoi : ")
        tournament_description = input("Vous pouvez ajouter une description : ")
        return tournament_name, tournament_location, tournament_description

    @staticmethod
    def prompt_open_tournament():
        """Prompt pour selectionner le tournoi et receuillir la date de début d'ouverture """
        tournament_name = input("Veuillez entrer le nom du tournoi \n(taper x pour revnir au menu principal) :")
        if tournament_name == "x":
            return tournament_name
        if tournament_name != "x":
            open_date_tournament = View.test_date(input("Veuillez entrer la date de début du tournoi : "))
            datas_open_tournament = [tournament_name, open_date_tournament]
            return datas_open_tournament

    @staticmethod
    def prompt_create_players():
        """Prompt pour gérer la création d'un ou de plusieurs users"""
        lauch = input("\nVoulez vous enregistrer un nouveau joueur ? y/n ")
        return lauch

    @staticmethod
    def prompt_datas_player():
        """Prompt pour récupéré les données d'un user à inscrire"""
        print("\nEnregistrement des joueurs")
        first_name = input("\nVeuillez indiquer le prénom du joueur : ")
        last_name = input("Veuillez indiquer le nom du joueur : ")
        date_of_birth = View.test_date(input
                                       ("Veuillez indiquer la date de naissance du joueur sous le format jj/mm/yy : "))
        return first_name, last_name, date_of_birth

    @staticmethod
    def prompt_choice_tournament():
        tournament_name = input("\nVeuillez indiquer le nom du tournoi : ")
        return tournament_name

    @staticmethod
    def prompt_lauch_round():
        lauch = input("Voulez-vous lancer un nouveau round ? y/n ")
        return lauch

    @staticmethod
    def prompt_close_round():
        lauch = input("Voulez-vous cloturer le round en cours ? y/n ")
        return lauch

    def prompt_score_matchs(self, name_player1=None, name_player2=None):
        if self == 1:
            print("Entrer le résultat du match pour chaque joueur :\n")
            return
        elif self == 2:
            print("* Match opposant " + name_player1["first_name"] + " " + name_player1["last_name"] + " et "
                  + name_player2["first_name"] + " " + name_player2["last_name"])
            score = input("Score réalisé par " + name_player1["first_name"] + " " + name_player1["last_name"] + " : ")
            return score

    @staticmethod
    def prompt_search_tournament():
        """Prompt pour rechercher un tournoi """
        tournament_name = input("Veuillez entrer le nom du tournoi :\n")
        return tournament_name

    def prompt_search_players_tournament(self):
        """Prompt pour demander s'il faut effectuer l'affichage des joueurs """
        choice = input("\nVoulez-vous afficher la liste des joueurs du tournoi " + self["name"] + " ? (y/n)\n")
        return choice

    def prompt_search_rounds_tournament(self):
        """Prompt pour demander s'il faut effectuer l'affichage des rounds """
        choice = input("\nVoulez-vous afficher la liste des rounds du tournoi " + self["name"] + " ? (y/n)\n")
        return choice

    def prompt_search_matchs_tournament(self):
        """Prompt pour demander s'il faut effectuer l'affichage des matchs d'un round """
        choice = input("\nVoulez-vous afficher la liste des matchs d'un round du tournoi "
                       + self["name"] + " ? (y/n)\n")
        return choice

    @staticmethod
    def prompt_name_round():
        """Prompt pour demander le nom d'un round du tournoi et renvoi le nom"""
        round_name = input("\nEntrer le nom du round :\n")
        return round_name

    def display_register_player(self):
        """Affiche un message confirmant l'inscription du player"""
        print("===> Le joueur est inscrit au tournoi " + self + ".\n")

    def display_create_tournament(self):
        """Affiche un message confirmant la création du tournoi"""
        print("\n===> Le tournoi '" + self + "' est enregistré")

    def display_create_player(self, last_name):
        """Affiche un message confirmant l'inscription du player"""
        print("===> Le joueur " + self + " " + last_name + " est enregistré dans la base de joueurs.")

    def display_error_tournament(self):
        """Affiche un message indiquant que le tournoi n'existe pas"""
        print("Le tournoi " + self + " n'existe pas.")

    def display_open_tournament(self, start_date):
        """Affiche un message confirmant l'ouverture du tournoi"""
        print('le tournoi "' + self + '" est ouvert.')

    @staticmethod
    def display_error_menu():
        """Affiche un message indiquant une erreur sur le choix du sous menu"""
        print("Veuillez saisir un numéro existant.")

    def display_tournament_already_exist(self):
        """Affiche un message d'erreur car le tournoi existe déjà"""
        print('le tournoi "' + self + '" existe déjà.\n')

    @staticmethod
    def display_error_tournamentinprogress():
        """Affiche un message indiquant qu'un tournoi est deja en cours"""
        print("Un tournoi est déjà en cours, vous ne pouvez pas en ouvrir un second.\n")

    @staticmethod
    def display_error_tournament_already_closed():
        """Affiche un message indiquant qu'un tournoi est deja en cours"""
        print("Le tournoi est déjà clos, vous ne pouvez pas l'ouvrir une seconde fois.\n")

    @staticmethod
    def display_error_roundinprogress():
        """Affiche un message indiquant qu'un round est deja en cours"""
        print("Un round est déjà en cours, vous ne pouvez pas en ouvrir un second.\n")

    @staticmethod
    def display_error_roundnotinprogress():
        """Affiche un message indiquant qu'il n'y a aucun round en cours"""
        print("Aucun round en cours, vous ne pouvez pas cloturer de round.\n")

    @staticmethod
    def display_error_choise():
        """Affiche un message indiquant une erreur sur le choix"""
        print("\nMerci de répondre par y pour yes ou n pour no")

    @staticmethod
    def display_error_player_already_registrer():
        """Affiche un message indiquant une erreur sur le choix"""
        print("\nLe joueur est déjà inscrit sur ce tournoi.")

    @staticmethod
    def display_error_tournement_notinprogress():
        """Affiche un message indiquant qu'il n'y a pas de tourno en cours"""
        print("\nIl n'y a pas de tournoi en cours.\nVeuillez ouvrir un tournoi pour lancer un round.\n")

    def display_lauch_round(self):
        print("==> Le round " + self + " est lancé.\n")

    def display_close_round(self):
        print("==> Le round " + self + " est cloturé.\n")

    def display_close_tournament(self):
        print("==> Le tournoi " + self + " est cloturé.\n")

    def display_win_player(self):
        print(self["first_name"] + " " + self["last_name"] + " a gagné le match.\n")

    def display_equality_player(self, player_win2):
        print(self["first_name"] + " " + self["last_name"] + " " + player_win2["first_name"]
              + " " + player_win2["last_name"] + " ont fait match nul.\n")

    @staticmethod
    def display_error_score():
        print("Score incorrect.")

    @staticmethod
    def display_create_report():
        print("\nVotre rapport a été crée, il se trouve dans le dossier racine au format html.")

    def display_result_search_tournement(self):
        if self["end_date"] == "01/01/2000":
            if self["start_date"] == "01/01/2000":
                print("Le tournoi " + self["name"] + " n'est pas encore planifié.")
                return 0
            else:
                print("Le " + self["name"] + " est prévue le " + self["start_date"])
                return 1
        else:
            print("Le " + self["name"] + " a démarré le " + self["start_date"] +
                  " et s'est terminé le " + self["end_date"])
            return 2

    def display_players_tournement(self):
        """Affiche le nom complet d'un joueur"""
        print(self[0] + " " + self[1])

    def display_rounds_tournement(self):
        """Affiche le nom complet d'un joueur"""
        print(self)

    def display_match_winner(self, losing_player):
        print(self + " a reporté le match contre " + losing_player)

    def display_match_equality(self, player2):
        print(self + " et " + player2
              + " ont fait match nul.")

    def test_date(self):
        """Valide la saisie d'une date"""
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

    @staticmethod
    def display_report_menu():
        """Affichage du menu d'affichage des reports"""
        print("\nAffichage des raports\n")
        print("1. Afficher la liste des joueurs.")
        print("2. Afficher la liste des tournois.")
        print("3. Rechercher un tournoi.")
        print("4. Revenir au menu principal.\n")
