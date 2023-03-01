from prettytable import PrettyTable
from views import menuConstants as INPUT
from models.player import Player
from models.tournament import Tournament
class Reports():
    """classe des Rapports"""

    def __init__(self):
        pass

    @staticmethod
    def displayOfAllPlayers():
        """Affichage de tous les joueurs de tous les tournois"""
        listPlayers = Player.load()
        mytable = PrettyTable(['Nom','Prénom','Date_de_naissaice','le score'])
        for player in listPlayers:
            mytable.add_row([player.getFirstName(),player.getLastName(),player.getBirthday(),player.getScore()])
        mytable.sortby = "Nom"
        print(mytable)
       

    
    def displayOfPlayersByTournament():
        """Affichage des joueurs par tournoi donné"""
        tournamentChoice =  ""
        tournamentChoice = input(INPUT.STR_TOURNAMENT_NAME)
        while not tournamentChoice:
            tournamentChoice = input(INPUT.STR_TOURNAMENT_NAME)
        results = Tournament.db.search(Tournament.User._Tournament__name == tournamentChoice)

        while not results:
            tournamentChoice = input("le choix n'existe pas  ! veuillez en saisir un autre : ")
            results = Tournament.db.search(Tournament.User._Tournament__name == tournamentChoice)
            
        mytable = PrettyTable(['Nom','Prénom','Date_de_naissaice','le score'])

        for tournament in results:
          for player in tournament['_Tournament__playersList']:
              mytable.add_row([player['firstName'],player['lastName'],player['birthday'],player['leScore']])
        print(mytable)

    def displayOfAllTournaments():
        """Affichage de tous les tournoi existants"""
        listTournaments_dict = Tournament.load()
        mytable = PrettyTable(['Nom_du_tournoi','Location','Date'])
        for tournament in listTournaments_dict:
            mytable.add_row([tournament['_Tournament__name'],tournament['_Tournament__location'],tournament['_Tournament__dateTime']])
        print(mytable)

    def displayOfTournament():
        """Affichage de la date et nom d'un tournoi donné"""
        tournamentChoice =  ""
        tournamentChoice = input(INPUT.STR_TOURNAMENT_NAME)
        while not tournamentChoice:

            tournamentChoice = input(INPUT.STR_TOURNAMENT_NAME)

        results = Tournament.db.search(Tournament.User._Tournament__name == tournamentChoice)

        while not results:
            tournamentChoice = input("le choix n'existe pas  ! veuillez en saisir un autre : ")
            results = Tournament.db.search(Tournament.User._Tournament__name == tournamentChoice)

        mytable = PrettyTable(['Nom_du_tournoi','Location','Date'])

        for tournament in results:
            mytable.add_row([tournament['_Tournament__name'],tournament['_Tournament__location'],tournament['_Tournament__dateTime']])
        print(mytable)
        
    
    def displayOfallRoundsgamesByTournament(touramentChoice):
        """affichage de la liste de tous les tours du tournoi et de tous les matchs du tour """
        pass
