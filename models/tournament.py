""" Define instance_of_games"""
import datetime


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
