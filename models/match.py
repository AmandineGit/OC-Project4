""" Define match"""


class Match:
    """ Définition de la class Match """

    def __init__(self, score=None):
        if score is None:
            score = ()
        self.score = score

    def __repr__(self):
        """ représentation de l objet de type Match """
        return "Détails du match " + str(self.score)
