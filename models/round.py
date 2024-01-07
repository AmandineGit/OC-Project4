""" Define round"""
import datetime
from models.file_json import JsonFile

class Round:
    """ Définition de la class Round (tour) """
    start_date = datetime.date
    end_date = datetime.date

    def __init__(self, name, matchs_list=None, start_date="01/01/2000 12:00",
                 end_date="01/01/2000 12:00"):
        self.name = name
        if matchs_list is None:
            matchs_list = []
        self.matchs_list = matchs_list
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
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