""" Define main controllers."""
import random

from models.tournament import Tournament
from models.round import Round
from models.player import Player
from views.menu import View
from models.file_json import JsonFile
from datetime import datetime
import os


class Controllers:
    """Classe principale """
    @staticmethod
    def main_menu():
        """Gestion des sous menu avec une boucle infinie"""
        while True:
            View.display_main_menu()
            available_choices = (0, 1, 2, 3, 4, 5, 6)
            choice = View.prompt_main_menu()
            choice = int(choice)
            if choice not in available_choices:
                View.display_error_menu()
                continue
            elif choice == 1:
                Controllers.create_tournament()
            elif choice == 2:
                Controllers.open_tournament()
            elif choice == 3:
                Controllers.create_players()
            elif choice == 5:
                Controllers.lauch_round()
            elif choice == 6:
                View.prompt_finish_roud()

    @staticmethod
    def create_tournament():
        """Création d'un tournoi"""
        name, location = View.prompt_create_tournament()
        tournament_exist = Tournament.record_tournament(name, location)
        if tournament_exist is False:
            View.display_create_tournament(name)
        elif tournament_exist is True:
            View.display_tournament_already_exist(name)
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
                else:
                    View.display_error_tournament(tournament_name)
        Controllers.main_menu()


    @staticmethod
    def create_players():
        """Création et enregistrement sur un tournoi de users"""
        while True:
            """gestion du sous menu"""
            available_choices = ("n", "y")
            choice = View.prompt_create_players()
            if choice not in available_choices:
                View.display_error_choise()
                continue
            elif choice == "n":
                Controllers.main_menu()
            elif choice == "y":
                datas = View.prompt_datas_player()
                first_name, last_name, date_of_birth, tournament_name = datas
                tournament_exist = Tournament.search_tournament(tournament_name)
                if tournament_exist is False:
                    """si le tournoi saisie n'existe pas, le user est invité à saisir à nouveau"""
                    View.display_error_tournament(tournament_name)
                    continue
                else:
                    datas_player = first_name, last_name, date_of_birth
                    player_exist = Player.search_player(datas_player)
                    if player_exist is True:
                        Controllers.registrer_player_tournament(datas)
                    else:
                        """Si le player n'est pas encore connu, 
                        alors il est également enregistré dans le fichier players.json"""
                        player = Player(first_name, last_name, date_of_birth)
                        dataswip = datas
                        Player.record_player(player, "players.json")
                        View.display_create_player(first_name, last_name)
                        Controllers.registrer_player_tournament(dataswip)
                        break
            continue

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
        lauch = View.prompt_lauch_round()
        while lauch != "n" and lauch != "y":
            View.display_error_choise()
            lauch = View.prompt_lauch_round()
        if lauch == "n":
            return
        elif lauch == "y":
            current_date = datetime.now()
            current_date = current_date.strftime('%w/%m/%Y %H:%M')
            round_name = Controllers.name_of_round()

            current_tournament = (Tournament.current_tournament())
            last_round_in_tournament = Tournament.last_number_of_round(current_tournament.get("name"))
            current_tournament["rounds_list"].append(round_name)
            Tournament.update_tournament(current_tournament)

            matchs_list = Controllers.initialize_round(current_tournament, last_round_in_tournament)
            Round.record_round(round_name, current_date, matchs_list)
            View.display_lauch_round(round_name)
            return

    @staticmethod
    def name_of_round():
        """définie le nom d'un round"""
        if os.path.exists("rounds.json"):
            """génération du nom du round"""
            while Round.open_round_exist() is True:
                View.display_error_roundinprogress()
                Controllers.main_menu()
            last_round = Round.last_number_of_round()
            last_number = last_round[-1:]
            last_number = int(last_number)
            current_number = last_number + 1
            str(current_number)
            current_number = str(current_number)
            name_round = "Round" + current_number
            return name_round
        else:
            return "Round1"

    @staticmethod
    def initialize_round(self, last_round_in_tournament):
        """ Initialisation du round"""
        if last_round_in_tournament == 0:
            """lancer la premièrer initialisation, mélange aléatoire des joueurs"""
            registred_players_list = self["registred_players_list"]
            random.shuffle(registred_players_list)
            return registred_players_list
        else:
            """créer un nouveau round"""
            registred_players_list = current_tournament["registred_players_list"]
            random.shuffle(registred_players_list)
            return registred_players_list
