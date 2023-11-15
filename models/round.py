""" Define round"""
import datetime


class Round:
    """ Définition de la class Round (tour) """
    start_date = datetime.date
    end_date = datetime.date

    def __init__(self, name, matchs_list=None, start_date="01/01/2000",
                 end_date="01/01/2000"):
        self.name = name
        if matchs_list is None:
            matchs_list = []
        self.matchs_list = matchs_list
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        """ représentation de l objet de type Round """
        return self.name
