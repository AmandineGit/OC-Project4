""" Define instance_of_games"""
import datetime
from models.file_json import JsonFile


class Tournament:
    """ Définition de la class Tournament (tournoi) """
    start_date = datetime.date
    end_date = datetime.date

    def __init__(self, name, location, registred_players_list=None, number_of_round=4, description="",
                 start_date="01/01/2000", rounds_list=None, current_round_number=0, end_date="01/01/2000"):
        self.name = name
        self.location = location
        if registred_players_list is None:
            registred_players_list = []
        self.registred_players_list = registred_players_list
        if rounds_list is None:
            self.rounds_list = []
        self.number_of_round = number_of_round
        self.description = description
        self.start_date = start_date
        self.current_round_number = current_round_number
        self.end_date = end_date

    def __repr__(self):
        """ représentation de l objet de type Tournament"""
        return self.name

    def record_tournament(self, location):
        """création d'un tournoi"""
        tournament_exist = Tournament.search_tournament(self)
        if tournament_exist == Fasle :
            tournament = Tournament(self, location)
            json_file = tournament.__dict__
            json_tournament = JsonFile("tournaments.json", json_file)
            JsonFile.append_json(json_tournament)
        else:
            print("")

    def update_tournament(self):
        """Mise à jour du tournoi dans le json"""
        json_tournament = JsonFile("tournaments.json", [])
        tournaments_list = JsonFile.read_json(json_tournament)
        for i, tournament in enumerate(tournaments_list) :
            if tournament.get("name") == self["name"]:
                index = i
        if index != -1:
            tournaments_list[index]=self
        json_tournament.datas_json = tournaments_list
        JsonFile.create_json(json_tournament)

    def search_tournament(self):
        """Test d'existance d'un tournoi"""
        json_tournaments = JsonFile("tournaments.json", [])
        tournaments = JsonFile.read_json(json_tournaments)
        for tournament in tournaments:
            if tournament.get("name") == self:
                return True
        return False




