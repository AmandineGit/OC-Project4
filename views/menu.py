""" Define menu"""
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
        """Prompt pour créer un tournoi qui ensuite
        lance le prompt pour la création des players"""
        print("\n===> Création du Tournoi")
        tournament_location \
            = input("\nVeuillez indiquer le lieu du tournoi : ")
        tournament_name \
            = input("Veuillez indiquer le nom du tournoi : ")
        tournament_description \
            = input("Vous pouvez ajouter une description : ")
        return tournament_name, tournament_location, tournament_description

    @staticmethod
    def prompt_open_tournament():
        """Prompt pour selectionner le tournoi
        et receuillir la date de début d'ouverture """
        tournament_name\
            = input("Veuillez entrer le nom du tournoi"
                    " \n(taper x pour revnir au menu principal) :")
        if tournament_name == "x":
            return tournament_name
        if tournament_name != "x":
            open_date_tournament = (
                View.test_date(
                    input("Veuillez entrer la date de début du tournoi : ")
                )
            )
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
        date_of_birth = (View.test_date
                         (input("Veuillez indiquer la date de naissance "
                                "du joueur sous le format jj/mm/yy : ")))
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

    @staticmethod
    def prompt_score_matchs(action, name_player1=None, name_player2=None):
        if action == 1:
            print("Entrer le résultat du match pour chaque joueur :\n")
            return
        elif action == 2:
            print("* Match opposant " + name_player1["first_name"]
                  + " " + name_player1["last_name"] + " et "
                  + name_player2["first_name"] + " "
                  + name_player2["last_name"])
            score = input("Score réalisé par "
                          + name_player1["first_name"]
                          + " " + name_player1["last_name"] + " : ")
            return score

    @staticmethod
    def prompt_search_tournament():
        """Prompt pour rechercher un tournoi """
        tournament_name = input("Veuillez entrer le nom du tournoi :\n")
        return tournament_name

    @staticmethod
    def prompt_search_players_tournament(tournament):
        """Prompt pour demander s'il faut effectuer l'affichage des joueurs """
        choice = input("\nVoulez-vous afficher la liste des joueurs du tournoi"
                       + tournament["name"] + " ? (y/n)\n")
        return choice

    @staticmethod
    def prompt_search_rounds_tournament(tournament):
        """Prompt pour demander s'il faut effectuer l'affichage des rounds """
        choice = input("\nVoulez-vous afficher la liste des rounds du tournoi "
                       + tournament["name"] + " ? (y/n)\n")
        return choice

    @staticmethod
    def prompt_search_matchs_tournament(tournament):
        """Prompt pour demander s'il faut effectuer
        l'affichage des matchs d'un round """
        choice = input("\nVoulez-vous afficher "
                       "la liste des matchs d'un round du tournoi "
                       + tournament["name"] + " ? (y/n)\n")
        return choice

    @staticmethod
    def prompt_name_round():
        """Prompt pour demander le nom d'un round
        du tournoi et renvoi le nom"""
        round_name = input("\nEntrer le nom du round :\n")
        return round_name

    @staticmethod
    def display_register_player(tournament):
        """Affiche un message confirmant l'inscription du player"""
        print("===> Le joueur est inscrit au tournoi " + tournament + ".\n")

    @staticmethod
    def display_create_tournament(tournament):
        """Affiche un message confirmant la création du tournoi"""
        print("\n===> Le tournoi '" + tournament + "' est enregistré")

    @staticmethod
    def display_create_player(first_name, last_name):
        """Affiche un message confirmant l'inscription du player"""
        print("===> Le joueur " + first_name + " "
              + last_name + " est enregistré dans la base de joueurs.")

    @staticmethod
    def display_error_tournament(tournament):
        """Affiche un message indiquant que le tournoi n'existe pas"""
        print("Le tournoi " + tournament + " n'existe pas.")

    @staticmethod
    def display_open_tournament(tournament, start_date):
        """Affiche un message confirmant l'ouverture du tournoi"""
        print('le tournoi "' + tournament + '" est ouvert.')

    @staticmethod
    def display_error_menu():
        """Affiche un message indiquant une erreur sur le choix du sous menu"""
        print("Veuillez saisir un numéro existant.")

    @staticmethod
    def display_tournament_already_exist(tournament):
        """Affiche un message d'erreur car le tournoi existe déjà"""
        print('le tournoi "' + tournament + '" existe déjà.\n')

    @staticmethod
    def display_error_tournamentinprogress():
        """Affiche un message indiquant qu'un tournoi est deja en cours"""
        print("Un tournoi est déjà en cours, "
              "vous ne pouvez pas en ouvrir un second.\n")

    @staticmethod
    def display_error_tournament_already_closed():
        """Affiche un message indiquant qu'un tournoi est deja en cours"""
        print("Le tournoi est déjà clos, "
              "vous ne pouvez pas l'ouvrir une seconde fois.\n")

    @staticmethod
    def display_error_roundinprogress():
        """Affiche un message indiquant qu'un round est deja en cours"""
        print("Un round est déjà en cours,"
              " vous ne pouvez pas en ouvrir un second.\n")

    @staticmethod
    def display_error_roundnotinprogress():
        """Affiche un message indiquant qu'il n'y a aucun round en cours"""
        print("Aucun round en cours,"
              " vous ne pouvez pas cloturer de round.\n")

    @staticmethod
    def display_error_nb_players():
        """Affiche un message indiquant qu'il n'y a pas assez
         de joeurs pour démarrer le tournoi"""
        print("Il n'y a pas assez de joueurs inscrits sur ce tournoi.\n")

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
        print("\nIl n'y a pas de tournoi en cours."
              "\nVeuillez ouvrir un tournoi pour lancer un round.\n")

    @staticmethod
    def display_lauch_round(round_name):
        print("==> Le round " + round_name + " est lancé.\n")

    @staticmethod
    def display_close_round(round_name):
        print("==> Le round " + round_name + " est cloturé.\n")

    @staticmethod
    def display_close_tournament(tournament):
        print("==> Le tournoi " + tournament + " est cloturé.\n")

    @staticmethod
    def display_win_player(player_win):
        """Affiche les résutats d'un match"""
        print(player_win["first_name"] + " "
              + player_win["last_name"] + " a gagné le match.\n")

    @staticmethod
    def display_equality_player(player_win, player_win2):
        """Affiche les résutats d'un match"""
        print(player_win["first_name"] + " "
              + player_win["last_name"] + " "
              + player_win2["first_name"]
              + " " + player_win2["last_name"]
              + " ont fait match nul.\n")

    @staticmethod
    def display_error_score():
        """message d erreur de saisie"""
        print("Score incorrect.")

    @staticmethod
    def display_create_report():
        print("\nVotre rapport a été crée,"
              " il se trouve dans le dossier racine au format html.")

    @staticmethod
    def display_result_search_tournement(tournament):
        """affiche les dates d'un tournoi"""
        if tournament["end_date"] == "01/01/2000":
            if tournament["start_date"] == "01/01/2000":
                print("Le tournoi "
                      + tournament["name"]
                      + " n'est pas encore planifié.")
                return 0
            else:
                print("Le "
                      + tournament["name"] +
                      " est prévue le "
                      + tournament["start_date"])
                return 1
        else:
            print("Le "
                  + tournament["name"] +
                  " a démarré le "
                  + tournament["start_date"] +
                  " et s'est terminé le "
                  + tournament["end_date"])
            return 2

    @staticmethod
    def display_players_tournement(name_player):
        """Affiche le nom complet d'un joueur"""
        print(name_player[0] + " " + name_player[1])

    @staticmethod
    def display_rounds_tournement(round):
        """Affiche le nom complet d'un joueur"""
        print(round)

    @staticmethod
    def display_match_winner(win_player, losing_player):
        print(win_player + " a reporté le match contre " + losing_player)

    @staticmethod
    def display_match_equality(player1, player2):
        print(player1 + " et " + player2
              + " ont fait match nul.")

    @staticmethod
    def display_error_search_round():
        """Affiche un message d'erreur si le nom du round est érroné"""
        print("Veuillez entrer le nom d'un round existant,"
              " en respectant les majuscules et minuscules.")

    @staticmethod
    def test_date(date_str):
        """Valide la saisie d'une date"""
        test = False
        while test is False:
            try:
                datetime.strptime(date_str, "%d/%m/%Y")
                test = True
            except ValueError:
                print("Format de date incorrect. Veuillez réessayer.")
                date_str = input("Veuillez indiquer une date"
                                 " sous le format jj/mm/yy : ")
        return date_str

    @staticmethod
    def display_report_menu():
        """Affichage du menu d'affichage des reports"""
        print("\nAffichage des raports\n")
        print("1. Afficher la liste des joueurs.")
        print("2. Afficher la liste des tournois.")
        print("3. Rechercher un tournoi.")
        print("4. Revenir au menu principal.\n")
