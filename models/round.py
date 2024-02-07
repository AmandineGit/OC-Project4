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

    @staticmethod
    def record_round(round_name, start_date, matchs_list):
        """création d'un round  """
        round = Round(round_name, start_date, matchs_list)
        json_file = round.__dict__
        json_round = JsonFile("rounds.json", json_file)
        JsonFile.append_json(json_round)
        print("\n==> Le fichier " + "rounds.json" + " a été mis à jour")
        return round

    @staticmethod
    def open_round_exist():
        """recherche et renvoi un booleen et
        le dict du round en cours ou un str vide"""
        json_round = JsonFile("rounds.json", [])
        rounds = JsonFile.read_json(json_round)
        open_round_exist = False
        if rounds is not False:
            for round in rounds:
                if (round.get("start_date") != "01/01/2000 12:00"
                        and round.get("end_date") == "01/01/2000 12:00"):
                    open_round_exist = True
                    round_exist = round
                else:
                    open_round_exist = False
                    round_exist = ""
        else:
            open_round_exist = False
            round_exist = ""
        return [open_round_exist, round_exist]

    @staticmethod
    def last_number_of_round():
        """Recherche et renvoi le numéro du dernier round d'un tournoi"""
        json_rounds = JsonFile("rounds.json", [])
        rounds = JsonFile.read_json(json_rounds)
        if rounds is not False:
            return rounds[-1]["name"]
        else:
            return "Round0"

    @staticmethod
    def prompt_close_round():
        lauch = input("Voulez-vous cloturer le round en cours ? y/n ")
        return lauch

    @staticmethod
    def search_matchslist_round(name_round):
        """Renvoi la list des matchs d'un round à partir de son nom"""
        json_rounds = JsonFile("rounds.json", [])
        rounds = JsonFile.read_json(json_rounds)
        for round in rounds:
            if round.get("name") == name_round:
                return round.get("matchs_list")

    @staticmethod
    def update_round(current_round):
        """Mise à jour du round dans le json, à utiliser
        avec un object round complet pour avoir toutes
        les données du round"""
        json_round = JsonFile("rounds.json", [])
        rounds_list = JsonFile.read_json(json_round)
        index = -7
        for i, round in enumerate(rounds_list):
            if round.get("name") == current_round["name"]:
                index = i
        if index != -1:
            rounds_list[index] = current_round
        json_round.datas_json = rounds_list
        JsonFile.create_json(json_round)
        print("\n==> Le fichier " + "rounds.json" + " a été mis à jour")
