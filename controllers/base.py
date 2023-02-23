from controllers.menuController import MenuController
from datetime import datetime
from models.round import Round
from models.game import Game
from models.player import Player


class Base():
    """programme de base du lancement de l'application"""
    
    def __init__(self):
        pass

    @staticmethod
    def lanch():
        """lancement de l'application"""
        menu = MenuController()
        menu.startMenu()
    




        
        
    
   




