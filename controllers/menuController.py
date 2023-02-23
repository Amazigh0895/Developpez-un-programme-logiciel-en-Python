""" Menu de l'application """
from models.player import Player
from models.round import Round
from models.game import Game
from models.tournament import Tournament
from views import menuConstants as INPUT
from controllers.verifInputController import Input

class MenuController:
    """la classe menu """

    def __init__(self):
        pass

    @staticmethod
    def startMenu():
        """commencer la partie"""
        print(INPUT.MENU_TITLE)

        
        choice_input = [0 , 1 , 2]
        user_choice_input = ""

        while user_choice_input not in choice_input:
            try :
                user_choice_input = int(input(INPUT.MAIN_MENU))
            except:
                print(INPUT.ERROR_VALUE_INPUT)

        while user_choice_input != 0 :
            if user_choice_input == 1:
                tournament = MenuController.createTournament("")
                player = MenuController.createPlayers()
                
                # Choix du lancement de la partie
                choice3_input = [0 , 1]
                user_choice3_input = ""
                while user_choice3_input not in choice3_input:
                    try:
                        user_choice3_input = int(input(INPUT.STR_IF_START_GAME))
                    except:
                        print(INPUT.ERROR_VALUE_INPUT)

                while user_choice3_input != 0 :     
                    if user_choice3_input == 1 :

                        # Chargement des joueurs
                        listPlayers = player.load()

                        # Instantiation des objets Round et Game
                        round = Round("Round","")
                        game = Game(listPlayers)

                        # Lancement de la partie 
                        tournament.startRoundsGame(round,game)
                        user_choice3_input = 0 
                user_choice_input = 0 
            elif user_choice_input == 2:
                pass 
                        
        print(INPUT.END_GAME)  


    @staticmethod
    def createTournament(date):
        """Menu de creation des tournois"""
        tournament = None
        print(INPUT.MENU_TITLE_TOURNAMENT)       
        while INPUT.AVAILABLE_INPUT:
                    try:
                        name = input(INPUT.STR_TOURNAMENT_NAME)
                        location = input(INPUT.STR_TOURNAMENT_LOCATION)
                        numberOfRounds = int(input(INPUT.STR_TOURNAMENT_NUMBER_OF_ROUNDS))
                        comment = input(INPUT.STR_TOURNAMENT_COMMENT)
                        tournament = Tournament(name,location,date,numberOfRounds,comment)
                        INPUT.AVAILABLE_INPUT = False

                    except:
                        print(INPUT.ERROR_VALUE_INPUT)
                        INPUT.AVAILABLE_INPUT = True
      

        print(INPUT.STR_TOURNAMENT_SAVED)

        return tournament

    @staticmethod
    def createPlayers():
        """Menu de creation des joueurs"""
        print(INPUT.MENU_TITLE_PLAYER)

        choice2_input = [0 , 1]
        user_choice2_input = 1
        while user_choice2_input  != 0 :

            firstName = input(INPUT.STR_PLAYER_FIRSTNAME)
            lastName = input(INPUT.STR_PLAYER_LASTNAME)
            birthday = input(INPUT.STR_PLAYER_BIRTHDAY)

            """Ajout des joueurs"""
            player = Player(firstName,lastName,birthday,0)
            player.save()
            print(INPUT.STR_PLAYER_SAVED)
            user_choice2_input = ""
            while user_choice2_input not in choice2_input :

                try :
                    user_choice2_input  = int(input(INPUT.STR_IF_ADD_NEW_PLAYER))
                except:
                    print(INPUT.ERROR_VALUE_INPUT)
           
     
        print("Nous avons terminé de créer les joueurs")
        return player

    
  
 
