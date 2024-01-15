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
                Controllers.player_registration()
            elif choice == 5:
                Controllers.lauch_round()
            elif choice == 6:
                Controllers.close_round()

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
    def player_registration():
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
                datas_player = datas
                player_id_exist = Player.search_player(datas_player)
                if player_id_exist is not False:
                    """si le player existe déjà il est inscrit directement au tournoi"""
                    Controllers.registrer_player_tournament(player_id_exist)
                else:
                    """si le player n'existe pas il est crée dans players.json puis inscrit au tournoi"""
                    national_chess_id = Controllers.create_player(datas_player)
                    View.display_create_player(datas_player[0], datas_player[1])
                    Controllers.registrer_player_tournament(national_chess_id)
                    break
            continue

    def create_player(self):
        """Si le player n'est pas encore connu,
        alors il est également enregistré dans le fichier players.json"""
        national_chess_id = Player.create_national_chess_id()
        first_name, last_name, date_of_birth = self
        player = Player(first_name, last_name, date_of_birth, national_chess_id)
        Player.record_player(player, "players.json")
        return national_chess_id

    def registrer_player_tournament(self):
        """Ajouter un player dans un tournoi
        Rechercher le tournoi en cours
        Ajouter le player dans la liste de players du tournoi grace à la methode update_tournament"""
        while True:
            tournament_name = View.prompt_choice_tournament()
            tournament_exist = Tournament.search_tournament(tournament_name)
            if tournament_exist is False:
                """si le tournoi saisie n'existe pas, le user est invité à saisir à nouveau"""
                View.display_error_tournament(tournament_name)
                continue
            elif tournament_exist is True:
                break
        json_tournament = JsonFile("tournaments.json", [])
        tournaments = JsonFile.read_json(json_tournament)
        for tournament in tournaments:
            if tournament.get("name") == tournament_name:
                players_list = tournament["registred_players_list"]
                if self not in players_list:
                    players_list.append(self)
                    tournament["registred_players_list"] = players_list
                    for tournamentnew in tournaments:
                        if tournamentnew.get("name") == tournament["name"]:
                            tournamentnew["registred_players_list"] = tournament["registred_players_list"]
                            Tournament.update_tournament(tournamentnew)
                    View.display_register_player(tournament_name)
                    return
                else:
                    View.display_error_player_already_registrer()
                    return

    @staticmethod
    def lauch_round():
        """Lancer un round"""
        while True:
            choice_available = ["y", "n"]
            choice = View.prompt_lauch_round()
            if choice not in choice_available:
                View.display_error_choise()
                continue
            elif choice == "n":
                Controllers.main_menu()
            elif choice == "y":
                current_date = datetime.now()
                current_date = current_date.strftime('%w/%m/%Y %H:%M')
                round_exist = Round.open_round_exist()
                while round_exist[0] is True:
                    View.display_error_roundinprogress()
                    Controllers.main_menu()
                round_name = Controllers.name_of_round()
                current_tournament = (Tournament.current_tournament())
                last_round_in_tournament = Tournament.last_number_of_round(current_tournament.get("name"))
                current_tournament["rounds_list"].append(round_name)
                round_number = round_name[5:]
                round_number = int(round_number)
                current_tournament["current_round_number"] = round_number
                Tournament.update_tournament(current_tournament)
                matchs_list = Controllers.initialize_round(current_tournament, last_round_in_tournament)
                Round.record_round(round_name, current_date, matchs_list)
                View.display_lauch_round(round_name)
                return

    @staticmethod
    def name_of_round():
        """définie le nom d'un round"""
        if os.path.exists("rounds.json"):
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
            new_registred_players_list = []
            registred_players_list = self["registred_players_list"]
            random.shuffle(registred_players_list)
            while True:
                if not registred_players_list:
                    break
                else:
                    pairs = registred_players_list[:2]
                    registred_players_list = registred_players_list[2:]
                    new_registred_players_list.append(pairs)
            return new_registred_players_list
        else:
            """A finiliser : créer un nouveau round"""
            new_registred_players_list = []
            registred_players_list = self["registred_players_list"]
            random.shuffle(registred_players_list)
            while True:
                if not registred_players_list:
                    break
                else:
                    pairs = registred_players_list[:2]
                    registred_players_list = registred_players_list[2:]
                    new_registred_players_list.append(pairs)
            print("no first round")
            return new_registred_players_list

    @staticmethod
    def close_round():
        while True:
            available_choices = ["y", "n"]
            choice = View.prompt_close_round()
            if choice not in available_choices:
                View.display_error_choise()
                continue
            elif choice == "n":
                Controllers.main_menu()
            elif choice == "y":
                current_round = Round.open_round_exist()
                if current_round[0] is False:
                    View.display_error_roundnotinprogress()
                    continue
                else:
                    current_round = current_round[1]
                    completed_matchs_tuple = Controllers.score_match()
                    current_date = datetime.now()
                    current_date = current_date.strftime('%w/%m/%Y %H:%M')
                    current_round["end_date"] = current_date
                    current_round["matchs_list"] = completed_matchs_tuple
                    Round.update_round(current_round)
                    View.display_close_round(current_round["name"])
                    return

    @staticmethod
    def score_match():
        current_round = Round.open_round_exist()
        matchs_list = current_round[1]["matchs_list"]
        View.prompt_score_matchs(1)
        completed_matchs_tuple = []
        for match in matchs_list:
            while True:
                name_player1 = Player.search_player_by_id(match[0])
                name_player2 = Player.search_player_by_id(match[1])
                score_player1 = View.prompt_score_matchs(2, name_player1, name_player2)
                possible_score = ["0", "1", "0.5"]
                if score_player1 not in possible_score:
                    View.display_error_score()
                    continue
                elif score_player1 == "1":
                    score_player2 = 0
                    player_win = match[0]
                    player_win = Player.search_player_by_id(player_win)
                    View.display_win_player(player_win)
                    break
                elif score_player1 == "0":
                    score_player2 = 1
                    player_win = match[1]
                    player_win = Player.search_player_by_id(player_win)
                    View.display_win_player(player_win)
                    break
                elif score_player1 == "0.5":
                    score_player2 = 0.5
                    player_win = match[0]
                    player_win2 = match[1]
                    player_win = Player.search_player_by_id(player_win)
                    player_win2 = Player.search_player_by_id(player_win2)
                    View.display_equality_player(player_win, player_win2)
                    break
            match_score = ([match[0], score_player1], [match[1], score_player2])
            completed_matchs_tuple.append(match_score)
            matchs_list = matchs_list[1:]
        return completed_matchs_tuple
