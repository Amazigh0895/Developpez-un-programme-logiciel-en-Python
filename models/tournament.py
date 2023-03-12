from tinydb import TinyDB, Query
from models.round import Round
from views import menuConstants as INPUT


class Tournament:
    """classe tournoi"""

    # Déclartation d'un variable static
    db = TinyDB('data/tournaments/list_tournament_Roundgames.json')
    dbPlayer = TinyDB('data/tournaments/list_players_by_tournament')
    User = Query()

    def __init__(self, name, location, dateTime,
                 numberOfRounds,
                 description):
        """initialisation des variables de notre tournoi

            ● nom
            ● lieu
            ● date de début et de fin
            ● nombre de tours,la valeur par défaut sur 4
            ● numéro correspondant au tour actuel
            ● une liste des tours
            ● une liste des joueurs enregistrés
            ● description pour les remarques générales du directeur du tournoi

        """
        self.__name = name
        self.__location = location
        self.__dateTime = dateTime
        self.__numberOfRounds = numberOfRounds
        self.__description = description
        self.__listRounds = {}
        self.__playersList = {}

    # Getters
    def getName(self):
        """retourne le nom du tournoi"""
        return self.__name

    def getLocation(self):
        """retourne la lieu du tournoi"""
        return self.__location

    def getDateTime(self):
        """retourne la date du tournoi"""
        return self.__dateTime

    def getNumberOfRounds(self):
        """retourne le nombre du tour du tournoi"""
        return self.__numberOfRounds

    def getplayersList(self):
        """retourne la liste des joueurs """
        from models.player import Player
        listPlayers = []
        for player in self.__playersList:
            listPlayers.append(Player(**player))
        return listPlayers

    def getListRounds(self):
        """retourne la liste des tours du tournoi"""
        return self.__listRounds

    def getDescription(self):
        """retourne la description du tournoi"""
        return self.__description

    # Setters
    def setName(self, name):
        """modifie le nom du tournoi"""
        self.__name = name

    def setLocation(self, location):
        """modifie la location du tournoi"""
        self.__location = location

    def setDateTime(self, dateTime):
        """modifie la date du tournoi"""
        self.__dateTime = dateTime

    def setNumbersOfRounds(self, numberOfRounds):
        """modifie la nombre de tours du tournoi"""
        self.__numberOfRounds = numberOfRounds

    def setDescription(self, description):
        """modifie la description du tournoi"""
        self.__description = description

    def setPlayerList(self, players):
        """modifie la liste des joueurs du tournoi"""
        self.__playersList = players

    # insertion des joueurs par tournoi--------------------------------------
    @staticmethod
    def addPlayer(player):
        """ajout des joueur d'un tournoi dans la base de donnée json"""
        Tournament.dbPlayer.insert(player.__dict__)

    @staticmethod
    def loadListPlayers():
        """methode static qui renvoi des donnees
        des joueurs d'un tournoi depuis la base de donnée json"""
        listPlayers_dict = Tournament.dbPlayer.all()
        return listPlayers_dict

    @staticmethod
    def resetPlayerDb():
        """réinitialise la base de donnée des joueurs d'un tournoi"""
        Tournament.dbPlayer.truncate()

    @staticmethod
    def resetDbRound():
        """reinitialise le fichier json a zéro"""
        Round.dbRoundTournament.truncate()

    # --------------------------------------------------------------------------
    @staticmethod
    def load():
        """charger tous les tournoi de la base de donnée"""
        listTournaments_dict = Tournament.db.all()
        return listTournaments_dict

    def setListGameRounds(self, listRounds):
        """modifie la listes des tours du tournoi"""
        self.__listRounds = listRounds

    def startRoundsGame(self, obj_round, obj_game):
        """declenche la partie en fonction du nombres de tours"""
        nbMax = self.getNumberOfRounds()
        for i in range(nbMax):
            obj_round.setName(f"Round{i+1}")
            print(INPUT.STR_START_GAME)
            print(obj_round.getName())
            obj_round.startGame(obj_game)

        self.setListGameRounds(Round.load())
        self.setPlayerList(Tournament.loadListPlayers())
        Tournament.save(self.__dict__)

    @staticmethod
    def save(tournament_round_dict):
        """sauvegarde la liste des tours
        des tournois dans la base de donnée json"""
        Tournament.db.insert(tournament_round_dict)
