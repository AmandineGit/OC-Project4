""" Define Person"""

class Person:
    """ Définition de la class Person"""

    def __init__(self, first_name, last_name):
        """ Initialisation de la class"""
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        """ représentation de l'objet de type Person"""
        return self.first_name + " " + self.last_name

roger = Person("Roger", "Rabbit")
print(roger)