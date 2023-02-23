from tinydb import TinyDB,Query
import json
class Player:
    """la classe joueur"""

    # Déclartation d'un variable static
    db = TinyDB('data/tournaments/list_of_players.json')
    User = Query()
    
    def __init__(self,firstName,lastName,birthday,leScore):
        """initialisation du joueur"""
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
        self.leScore = leScore
        
        
    # Getters
    def getFirstName(self):
        """renvoi le nom du joueur"""
        return self.firstName
    def getLastName(self):
        """renvoi le prenom du joueur"""
        return self.lastName
    def getScore(self):
        """renvois le score du joueur"""
        return self.leScore
    # Setters    
    def setScore(self,newScore):
        """reinitilise le score"""
        self.leScore += newScore
        Player.db.update({'leScore':self.leScore},Player.User.lastName ==f'{self.getLastName()}')
    
    def save(self):
        """sauvegarde la liste des joueurs dans la base de donnée json"""
        Player.db.insert(self.__dict__)
   
    @staticmethod
    def load():
        listPlayers = []
        """methode static qui renvoi des donnees des joueurs depuis la base de donnee json"""
        listPlayers_dict = Player.db.all()
        for player in listPlayers_dict:
            listPlayers.append(Player(**player))
        return listPlayers  
   
    def __repr__(self) -> str:
        """representation de l:'objet joueur"""
        return f"nom du joueur : {self.firstName} et son prenom : {self.lastName}"

        
        