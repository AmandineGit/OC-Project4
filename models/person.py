""" Define Player"""
import datetime


class Player:
    """ Création de la classe Player pour les players """
    date_of_birth = datetime.date

    def __init__(self, first_name, last_name, date_of_birth, national_chess_id=0, total_score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.national_chess_id = national_chess_id
        self.total_score = total_score

    def __repr__(self):
        """ représentation de l objet de type Person"""
        return self.first_name + " " + self.last_name
