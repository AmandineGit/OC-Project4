""" Define Person"""
import datetime
from abc import ABC


class Person(ABC):
    """ Définition de la class Person"""

    def __init__(self, first_name, last_name):
        """ Initialisation de la class"""
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        """ représentation de l objet de type Person"""
        return self.first_name + " " + self.last_name


class User(Person):
    """ Création de la sous_classe User pour les managers et le director """
    def __init__(self, first_name, last_name, login="", password="", enablement="0"):
        super().__init__(first_name, last_name)
        self.login = login
        self.password = password
        self.enablement = enablement


class Player(Person):
    """ Création de la sous_classe Player pour les players """
    date_of_birth = datetime.date

    def __init__(self, first_name, last_name, date_of_birth, national_chess_id=0, total_score=0):
        super().__init__(first_name, last_name)
        self.date_of_birth = date_of_birth
        self.national_chess_id = national_chess_id
        self.total_score = total_score
