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
            available_choices = (1, 2, 3, 4, 5, 6)
            choice = View.prompt_menu()
            try:
                choice = int(choice)
            finally:
                if choice not in available_choices:
                    View.display_error_menu()
                    continue
                elif choice == 1:
                    Controllers.create_tournament()
                elif choice == 2:
                    Controllers.open_tournament()
                elif choice == 3:
                    Controllers.player_registration()
                elif choice == 4:
                    Controllers.lauch_round()
                elif choice == 5:
                    Controllers.close_round()
                elif choice == 6:
                    Controllers.reports_submenu()

    @staticmethod
    def create_tournament():
        """Création d'un tournoi"""
        name, location, description = View.prompt_create_tournament()
        tournament_exist = Tournament.record_tournament(name, location, description=description)
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
                search_tournement = Tournament.search_tournament(tournament_name)
                if search_tournement[0] is True:
                    json_tournament = JsonFile("tournaments.json", [])
                    tournaments = JsonFile.read_json(json_tournament)
                    for tournament in tournaments:
                        if tournament.get("name") == datas_open_tournament[0]:
                            tournament["start_date"] = datas_open_tournament[1]
                            Tournament.update_tournament(tournament)
                            View.display_open_tournament(tournament_name, open_date)
                            Controllers.player_registration()
                elif search_tournement[0] == "already_closed":
                    View.display_error_tournament_already_closed()
                elif search_tournement is False:
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
            else:
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
                current_date = current_date.strftime('%d/%m/%Y %H:%M')
                try:
                    round_exist = Round.open_round_exist()
                except FileNotFoundError:
                    round_exist = [False, None]
                while round_exist[0] is True:
                    View.display_error_roundinprogress()
                    Controllers.main_menu()
                round_name = Controllers.name_of_round()
                current_tournament = (Tournament.current_tournament())
                nb_players = len(current_tournament["registred_players_list"])
                if current_tournament is None:
                    View.display_error_tournement_notinprogress()
                else:
                    while nb_players < 6:
                        View.display_error_nb_players()
                        Controllers.player_registration()
                    last_round_in_tournament = Tournament.last_number_of_round(current_tournament.get("name"))
                    current_tournament["rounds_list"].append(round_name)
                    round_number = round_name[5:]
                    round_number = int(round_number)
                    current_tournament["current_round_number"] = round_number
                    matchs_list = Controllers.create_pairs(current_tournament, last_round_in_tournament)
                    current_matchs_list = current_tournament["matchs_list"]
                    for match in matchs_list:
                        current_matchs_list.append(match)
                    current_tournament["matchs_list"] = current_matchs_list
                    Tournament.update_tournament(current_tournament)
                    Round.record_round(round_name, current_date, matchs_list)
                    View.display_lauch_round(round_name)
                return

    @staticmethod
    def name_of_round():
        """définie le nom d'un round"""
        if os.path.exists("rounds.json"):
            last_round = Round.last_number_of_round()
            last_number = last_round[5:]
            last_number = int(last_number)
            current_number = last_number + 1
            str(current_number)
            current_number = str(current_number)
            name_round = "Round" + current_number
            return name_round
        else:
            return "Round1"

    def create_pairs(self, last_round_in_tournament):
        """ Initialisation du round"""
        matchs_list = []
        registred_players_list = self["registred_players_list"]
        current_tournament = Tournament.current_tournament()
        tournament_matchs_list = current_tournament["matchs_list"]
        if last_round_in_tournament == 0:
            """lancer la premièrer initialisation, mélange aléatoire des joueurs"""
            random.shuffle(registred_players_list)
            for i in range(0, len(registred_players_list), 2):
                pairs = [registred_players_list[i], registred_players_list[i + 1]]
                matchs_list.append(pairs)
                pairs_inv = [pairs[1], pairs[0]]
                tournament_matchs_list.append(pairs_inv)
                tournament_matchs_list.append(pairs)
        else:
            """Créer la liste des matchs en triant les players 
            en fonction de leur score total en évitant les doublons"""
            sort_registred_players_list = Controllers.sort_players(registred_players_list)
            sort_registred_players_list = [couple[0] for couple in sort_registred_players_list]
            while len(sort_registred_players_list) >= 2:
                j = 2
                pairs = [sort_registred_players_list[0], sort_registred_players_list[1]]
                if len(sort_registred_players_list) >= 3:
                    while pairs in tournament_matchs_list:
                        pairs = [sort_registred_players_list[0], sort_registred_players_list[j]]
                        if j < len(sort_registred_players_list):
                            j += 1
                        else:
                            break
                pairs_inv = [pairs[1], pairs[0]]
                matchs_list.append(pairs)
                tournament_matchs_list.append(pairs_inv)
                tournament_matchs_list.append(pairs)
                sort_registred_players_list.remove(pairs[0])
                sort_registred_players_list.remove(pairs[1])

        current_tournament["matchs_list"] = tournament_matchs_list
        Tournament.update_tournament(current_tournament)
        return matchs_list

    def sort_players(self):
        """Tri une liste de joeurs en fonction de leur score et renvoi la liste triée avec les scores"""
        registred_players_list = []
        for player in self:
            datas_player = Player.search_player_by_id(player)
            registred_players_list.append([datas_player["national_chess_id"], datas_player["total_score"]])
        sort_registred_players_list = sorted(registred_players_list, key=lambda x: x[1])
        return sort_registred_players_list

    @staticmethod
    def close_round():
        available_choices = ["y", "n"]
        choice = View.prompt_close_round()
        if choice not in available_choices:
            View.display_error_choise()
            Controllers.main_menu()
        elif choice == "n":
            Controllers.main_menu()
        elif choice == "y":
            current_round = Round.open_round_exist()
            if current_round[0] is False:
                View.display_error_roundnotinprogress()
                Controllers.main_menu()
            else:
                current_round = current_round[1]
                completed_matchs_tuple = Controllers.score_match()
                current_date = datetime.now()
                current_date = current_date.strftime('%d/%m/%Y %H:%M')
                current_round["end_date"] = current_date
                current_round["matchs_list"] = completed_matchs_tuple
                Round.update_round(current_round)
                Controllers.player_score_keeping(completed_matchs_tuple)
                View.display_close_round(current_round["name"])
                Controllers.close_tournament()
                return

    @staticmethod
    def score_match():
        """recueille les scores des matchs grace à View.prompt_score_matchs
        puis créé une liste avec l'ID du player et son score"""
        current_round = Round.open_round_exist()
        matchs_list = current_round[1]["matchs_list"]
        View.prompt_score_matchs(1)
        completed_matchs_tuple = []
        for match in matchs_list:
            while True:
                player1 = Player.search_player_by_id(match[0])
                player2 = Player.search_player_by_id(match[1])
                score_player1 = View.prompt_score_matchs(2, player1, player2)
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
            match_score = ([match[0], float(score_player1)],
                           [match[1], float(score_player2)])
            completed_matchs_tuple.append(match_score)
            matchs_list = matchs_list[1:]
        return completed_matchs_tuple

    def player_score_keeping(self):
        """Calcul et met à jour le total_score des players dans players.json"""
        update_list_players = []
        for match in self:
            for player_score in match:
                player, score = player_score
                player_object = Player.search_player_by_id(player)
                if score == 1:
                    player_object["total_score"] = player_object["total_score"] + 1
                elif score == 0.5:
                    player_object["total_score"] = player_object["total_score"] + 0.5
                update_list_players.append(player_object)
        Player.update_player(update_list_players)

    @staticmethod
    def close_tournament():
        tournament = Tournament.current_tournament()
        if len(tournament["rounds_list"]) < 4:
            return
        else:
            current_date = datetime.now()
            current_date = current_date.strftime('%d/%m/%Y')
            tournament["end_date"] = current_date
            Tournament.update_tournament(tournament)
            View.display_close_tournament(tournament["name"])
            return

    @staticmethod
    def reports_submenu():
        """Gestion des sous menu avec une boucle infinie"""
        while True:
            View.display_report_menu()
            available_choices = (1, 2, 3, 4)
            choice = View.prompt_menu()
            try:
                choice = int(choice)
            finally:
                if choice not in available_choices:
                    View.display_error_menu()
                    continue
                elif choice == 1:
                    Controllers.display_players_report()
                elif choice == 2:
                    Controllers.display_tournaments_report()
                elif choice == 3:
                    Controllers.display_datas_tournament()
                elif choice == 4:
                    Controllers.main_menu()

    @staticmethod
    def display_players_report():
        """Affiche la liste des joueurs et l'enregistre
        dans un fichier html, la liste est classé par ordre alphabétique"""
        print("\n Liste des joueurs enregistrés :\n")
        json_player = JsonFile("players.json", [])
        players = JsonFile.read_json(json_player)
        sorted_players = sorted(players, key=lambda player: player["last_name"].lower())
        players_report = "RAPPORT : liste des joueurs enregistrés.<br><br><table border='1'>"
        sorted_players.insert(0, {"first_name": "Prénom", "last_name": "Nom",
                                  "date_of_birth": "Date de naissance", "national_chess_id": "ID",
                                  "total_score": "Score total"})
        for player in sorted_players:
            print(player["last_name"] + " " + player["first_name"])
            players_report += "<tr>"
            for cle, i in player.items():
                players_report += f"<td>{i}</td>"
            players_report += "</tr>"
        players_report += "</table>"
        with open("report_players.html", "w") as fichier:
            fichier.write(players_report)
        View.display_create_report()

    @staticmethod
    def display_tournaments_report():
        """Affiche la liste des tournois et l'enregistre
        dans un fichier html, la liste est classé par ordre alphabétique"""
        print("\n Liste des tournois enregistrés :\n")
        json_tournaments = JsonFile("tournaments.json", [])
        tournaments = JsonFile.read_json(json_tournaments)
        for tournament in tournaments:
            for cle in list(tournament.keys()):
                if cle != "name" and cle != "location":
                    tournament.pop(cle)
        tournaments_report = "RAPPORT : liste des tournois enregistrés.<br><br><table border='1'>"
        tournaments.insert(0, {"name": "Nom du tournoi", "location": "Lieu"})
        for tournament in tournaments:
            if tournament["name"] != "Nom du tournoi":
                print(tournament["name"] + " à " + tournament["location"])
            tournaments_report += "<tr>"
            for cle, i in tournament.items():
                tournaments_report += f"<td>{i}</td>"
            tournaments_report += "</tr>"
        tournaments_report += "</table>"
        with open("report_tournaments.html", "w") as fichier:
            fichier.write(tournaments_report)
        View.display_create_report()

    @staticmethod
    def display_datas_tournament():
        """Affiche les infos d'un tournoi, dates, joueurs, rounds, matchs"""
        name_tournament = View.prompt_search_tournament()
        return_search_tournament = Tournament.search_tournament(name_tournament)
        if return_search_tournament is False:
            View.display_error_tournament(name_tournament)
            Controllers.reports_submenu()
        else:
            pass
        tournament = return_search_tournament[1]
        View.display_result_search_tournement(tournament)

        while True:
            choice_available = ["y", "n"]
            choice = View.prompt_search_players_tournament(tournament)
            if choice not in choice_available:
                View.display_error_choise()
                continue
            elif choice == "n":
                Controllers.reports_submenu()
            elif choice == "y":
                for player in tournament["registred_players_list"]:
                    object_player = Player.search_player_by_id(player)
                    name_player = [object_player["last_name"], object_player["first_name"]]
                    View.display_players_tournement(name_player)
                break

        while True:
            choice_available = ["y", "n"]
            choice = View.prompt_search_rounds_tournament(tournament)
            if choice not in choice_available:
                View.display_error_choise()
                continue
            elif choice == "n":
                Controllers.reports_submenu()
            elif choice == "y":
                for round in tournament["rounds_list"]:
                    View.display_rounds_tournement(round)
                break

        while True:
            choice_available = ["y", "n"]
            choice = View.prompt_search_matchs_tournament(tournament)
            if choice not in choice_available:
                View.display_error_choise()
                continue
            elif choice == "n":
                Controllers.reports_submenu()
            elif choice == "y":
                name_round = View.prompt_name_round()
                matchs_list = Round.search_matchslist_round(name_round)
                try:
                    for match in matchs_list:
                        if match[0][1] == 1.0:
                            winning_player = match[0][0]
                            winning_player = (Player.search_player_by_id(winning_player)["first_name"]
                                              + " " + Player.search_player_by_id(winning_player)["last_name"])
                            losing_player = match [1][0]
                            losing_player = (Player.search_player_by_id(losing_player)["first_name"]
                                             + " " + Player.search_player_by_id(losing_player)["last_name"])
                            View.display_match_winner(winning_player, losing_player)
                        elif match[0][1] == 0.0:
                            losing_player = match[0][0]
                            losing_player = (Player.search_player_by_id(losing_player)["first_name"]
                                             + " " + Player.search_player_by_id(losing_player)["last_name"])
                            winning_player = match [1][0]
                            winning_player = (Player.search_player_by_id(winning_player)["first_name"]
                                              + " " + Player.search_player_by_id(winning_player)["last_name"])
                            View.display_match_winner(winning_player, losing_player)
                        if match[0][1] == 0.5:
                            player = match[0][0]
                            player = (Player.search_player_by_id(player)["first_name"]
                                      + " " + Player.search_player_by_id(player)["last_name"])
                            player2 = match [1][0]
                            player2 = (Player.search_player_by_id(player2)["first_name"]
                                       + " " + Player.search_player_by_id(player2)["last_name"])
                            View.display_match_equality(player, player2)
                except TypeError:
                    View.display_error_search_round()
                continue
