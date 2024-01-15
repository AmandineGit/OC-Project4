""" Define round"""
import datetime
from models.file_json import JsonFile


class Round:
    """ Définition de la class Round (tour) """
    start_date = datetime.date
    end_date = datetime.date

    def __init__(self, name, start_date="01/01/2000 12:00", matchs_list=None,
                 end_date="01/01/2000 12:00"):
        self.name = name
        self.start_date = start_date
        if matchs_list is None:
            matchs_list = []
        self.matchs_list = matchs_list
        self.end_date = end_date

    def __str__(self):
        """ représentation de l objet de type Round """
        return self.name

    def record_round(self, start_date, matchs_list):
        """création d'un round  """
        round = Round(self, start_date, matchs_list)
        json_file = round.__dict__
        json_round = JsonFile("rounds.json", json_file)
        JsonFile.append_json(json_round)
        print("\n==> Le fichier " + "rounds.json" + " a été mis à jour")
        return round

    @staticmethod
    def open_round_exist():
        """recherche et renvoi un booleen et le nom round en cours ou un str vide"""
        json_round = JsonFile("rounds.json", [])
        rounds = JsonFile.read_json(json_round)
        open_round_exist = False
        for round in rounds:
            if (round.get("start_date") != "01/01/2000 12:00"
                    and round.get("end_date") == "01/01/2000 12:00"):
                open_round_exist = True
                name_round_exist = round.get("name")
            else:
                open_round_exist = False
                name_round_exist = ""
        return [open_round_exist, name_round_exist]

    @staticmethod
    def last_number_of_round():
        """Recherche et renvoi le numéro du dernier round d'un tournoi"""
        json_rounds = JsonFile("rounds.json", [])
        rounds = JsonFile.read_json(json_rounds)
        return rounds[-1]["name"]

    @staticmethod
    def prompt_close_round():
        lauch = input("Voulez-vous cloturer le round en cours ? y/n ")
        return lauch

    def search_matchslist_round(self):
        """Renvoi la list des matchs d'un round """
        json_rounds = JsonFile("rounds.json", [])
        rounds = JsonFile.read_json(json_rounds)
        for round in rounds:
            if round.get("name") == self:
                return round.get("matchs_list")

    """def update_round(self):
        ""non utilise : 
        Mise à jour du round dans le json, à utiliser
        avec un object round complet pour avoir toutes les données du round""
        round = self.__dict__
        json_round = JsonFile("rounds.json", [])
        rounds_list = JsonFile.read_json(json_round)
        index = -7
        for i, round in enumerate(rounds_list):
            if round.get("name") == round["name"]:
                index = i
        if index != -1:
            rounds_list[index] = round
        json_round.datas_json = rounds_list
        JsonFile.create_json(json_round)"""

    """def search_round(self):
        "" Non utilisé Test d'existance d'un round""
        json_rounds = JsonFile("rounds.json", [])
        rounds = JsonFile.read_json(json_rounds)
        print(rouds)
        for round in rounds:
            if round.get("name") == self:
                return True
        return False"""