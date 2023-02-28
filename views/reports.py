from models.player import Player
from prettytable import PrettyTable
class Reports():
    """classe des Rapports"""

    def __init__(self):
        pass

    @staticmethod
    def displayOfAllPlayers():
        """Affichage de tous les joueurs de tous les tournois"""
        list = Player.load()
        mytable =PrettyTable(['Nom','Prénom','Date_de_naissaice','rang'])
        print(mytable)
        for player in list:
            mytable.add_row([player.getFirstName(),player.getLastName(),player.getBirthday(),player.getScore()])
        mytable.sortby = "Nom"
        print(mytable)
       
    
    def displayOfPlayersByTournament(touramentChoice):
        """Affichage des joueurs par tournoi donné"""
        pass

    def displayOfAllTournaments():
        """Affichage de tous les tournoi existants"""
        pass
    def displayOfTournament(touramentChoice):
        """Affichage de la date et nom d'un tournoi donné"""
        pass
    
    def displayOfallRoundsgamesByTournament(touramentChoice):
        """affichage de la liste de tous les tours du tournoi et de tous les matchs du tour """
        pass
