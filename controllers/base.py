from controllers.menuController import MenuController


class Base():
    """programme de base du lancement de l'application"""
    def __init__(self):
        pass

    @staticmethod
    def lanch():
        """lancement de l'application"""
        menu = MenuController()
        menu.startMenu()
