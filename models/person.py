""" Define Person"""
from abc import ABC

class Person(ABC):
    """ Définition de la class Person"""

    def __init__(self, first_name, last_name):
        """ Initialisation de la class"""
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        """ représentation de l'objet de type Person"""
        return self.first_name + " " + self.last_name

class User(Person):
    """ Création de la sous_classe User pour les managers et le directeur """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

roger = User("Roger", "Rabbit")
print(roger)