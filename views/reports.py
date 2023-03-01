from prettytable import PrettyTable
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
        mytable = PrettyTable(['Nom','Prénom','Date_de_naissaice','rang'])
        for player in listPlayers:
            mytable.add_row([player.getFirstName(),player.getLastName(),player.getBirthday(),player.getScore()])
        mytable.sortby = "Nom"
        print(mytable)
       
    
    def displayOfPlayersByTournament(touramentChoice):
        """Affichage des joueurs par tournoi donné"""
        pass

    def displayOfAllTournaments():
        """Affichage de tous les tournoi existants"""
        listTournaments_dict = Tournament.load()
        mytable = PrettyTable(['Nom_du_tournoi','Location','Date'])
        for tournament in listTournaments_dict:
            mytable.add_row([tournament['_Tournament__name'],tournament['_Tournament__location'],tournament['_Tournament__dateTime']])
        print(mytable)
        
    def displayOfTournament(touramentChoice):
        """Affichage de la date et nom d'un tournoi donné"""
        pass
    
    def displayOfallRoundsgamesByTournament(touramentChoice):
        """affichage de la liste de tous les tours du tournoi et de tous les matchs du tour """
        pass
