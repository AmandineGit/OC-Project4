""" Define main controllers."""
import json
import sys
sys.path.append("/home/mandine/PycharmProjects/OC-Project4/")
from models.tournament import Tournament


class Controllers:
    """Classe principale """

    def create_tournament(self, location):
        tournament = Tournament(self, location)
        try:
            with open("tournament.json", "a") as f:
                json.dump(tournament.__dict__, f)
        except Exception:
            print("Erreur lors de l'enregistrement du fichier tournament.json .")
