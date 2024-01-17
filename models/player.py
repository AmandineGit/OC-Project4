""" Define Player"""
import datetime
from models.file_json import JsonFile


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
        """ représentation de l objet de type Player"""
        return self.first_name + " " + self.last_name

    def record_player(self, name_file):
        """ enregistrement de l objet de type Player et relance la demande d'inscription pour un autre player"""
        json_file = self.__dict__
        json_player = JsonFile(name_file, json_file)
        JsonFile.append_json(json_player)

    def search_player(self):
        """Test d'existance d'un user"""
        first_name, last_name, date_of_birth = self
        json_player = JsonFile("players.json", [])
        players = JsonFile.read_json(json_player)
        for player in players:
            if (player.get("last_name") == last_name
                    and player.get("first_name") == first_name)\
                    and player.get("date_of_birth") == date_of_birth:
                return player.get("national_chess_id")
        return False

    @staticmethod
    def create_national_chess_id():
        json_player = JsonFile("players.json", [])
        players = JsonFile.read_json(json_player)
        last_player = players[-1]
        last_national_chess_id = last_player["national_chess_id"]
        last_national_chess_id = int(last_national_chess_id)
        next_national_chess_id = last_national_chess_id + 1
        return next_national_chess_id

    def search_player_by_id(self):
        """recherche un player par son ID et renvoi son l'object sous forme de dictionnaire,
        s'il n'existe pas il renvoie None"""
        json_player = JsonFile("players.json", [])
        players = JsonFile.read_json(json_player)
        for player in players:
            if player.get("national_chess_id") == self:
                return player


    def update_player(self):
        """met à jour un liste de players"""
        json_players = JsonFile("players.json", [])
        players_list = JsonFile.read_json(json_players)
        index = -7
        for new_player in self:
            for i, player in enumerate(players_list):
                if player.get("national_chess_id") == new_player["national_chess_id"]:
                    index = i
            if index != -1:
                players_list[index] = new_player
        json_players.datas_json = players_list
        JsonFile.create_json(json_players)
        print("\n==> Le fichier " + "players.json" + " a été mis à jour")
