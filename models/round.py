""" Define round"""
import datetime
from models.file_json import JsonFile


class Round:
    """ Définition de la class Round (tour) """
    start_date = datetime.date
    end_date = datetime.date

    def __init__(self, name, start_date="01/01/2000 12:00", matchs_list=None,
                 end_date="01/01/2000 12:00"):
        self.name = name
        self.start_date = start_date
        if matchs_list is None:
            matchs_list = []
        self.matchs_list = matchs_list
        self.end_date = end_date

    def __str__(self):
        """ représentation de l objet de type Round """
        return self.name

    def last_number_of_round(self):
        """Recherche et renvoi le numéro du dernier round terminé"""
        json_tournament = JsonFile("tournaments.json", [])
        tournaments = JsonFile.read_json(json_tournament)
        for tournament in tournaments:
            if tournament.get("name") == self:
                last_round_number = tournament.get("current_round_number")
                return last_round_number

    def record_round(self, start_date):
        """création d'un round  """
        round = Round(self, start_date)
        json_file = round.__dict__
        json_round = JsonFile("rounds.json", json_file)
        JsonFile.append_json(json_round)
        return round


    def search_round(self):
        """Test d'existance d'un d"""
        json_rounds = JsonFile("rounds.json", [])
        rounds = JsonFile.read_json(json_rounds)
        print(rouds)
        for round in rounds:
            if round.get("name") == self:
                return True
        return False
