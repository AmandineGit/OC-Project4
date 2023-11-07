""" Define instance_of_games"""
import datetime


class Tournament:
    """ Définition de la class Tournament (tournoi) """
    start_date = datetime.date
    end_date = datetime.date

    def __init__(self, name, tournament_number, location, registred_players_list=None, number_of_round=4,
                 description="", start_date="01/01/2000", current_round_number=0, end_date="01/01/2000"):
        self.name = name
        self.tournament_number = tournament_number
        self.location = location
        if registred_players_list is None:
            registred_players_list = []
        self.registred_players_list = registred_players_list
        self.number_of_round = number_of_round
        self.description = description
        self.start_date = start_date
        self.current_round_number = current_round_number
        self.end_date = end_date

    def __repr__(self):
        """ représentation de l objet de type Tournament"""
        return self.name


class Round:
    """ Définition de la class Round (tour) """
    start_date = datetime.date
    end_date = datetime.date

    def __init__(self, name, round_number, tournament_number, matchs_list=None, start_date="01/01/2000",
                 end_date="01/01/2000", scores_list=None):
        self.name = name
        self.round_number = round_number
        self.tournament_number = tournament_number
        if matchs_list is None:
            matchs_list = []
        self.matchs_list = matchs_list
        self.start_date = start_date
        self.end_date = end_date
        if scores_list is None:
            scores_list = []
        self.scores_list = scores_list

    def __repr__(self):
        """ représentation de l objet de type Round """
        return self.name + " du tournoi n°" + str(self.tournament_number)

class Match:
    """ Définition de la class Match """

    def __init__(self, match_number, tournament_number, round_number, match_players_color_list=None, score=None):
        self.match_number = match_number
        self.tournament_number = tournament_number
        self.round_number = round_number
        if match_players_color_list is None:
            match_players_color_list = []
        self.match_players_color_list = match_players_color_list
        if score is None:
            score = {}
        self.score = score

    def __repr__(self):
        """ représentation de l objet de type Match """
        return ("Match n°" + str(self.match_number) + " du round n°" + str(self.round_number)
                + " du tournoi n°" + str(self.tournament_number))
