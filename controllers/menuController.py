""" Menu de l'application """
from models.player import Player
from models.round import Round
from models.game import Game
from models.tournament import Tournament
from views import menuConstants as INPUT
from controllers.inputController import Input 
from views.reports import Reports
from datetime import datetime

class MenuController:
    """la classe menu """

    def __init__(self):
        pass

    @staticmethod
    def startMenu():
        """commencer la partie"""  
        print(INPUT.MENU_TITLE)
        
        choice_input = [0 , 1 , 2]
        user_choice_input = Input.makeRightChoiceInput(choice_input,INPUT.MAIN_MENU)

        while user_choice_input != 0 :
            if user_choice_input == 1:
                tournament = MenuController.createTournament(str(datetime.now()))
                MenuController.createPlayers(tournament)
                
                # Choix du lancement de la partie
                choice3_input = [0 , 1]
                user_choice3_input = Input.makeRightChoiceInput(choice3_input,INPUT.STR_IF_START_GAME)
                    
                while user_choice3_input != 0 :     
                    if user_choice3_input == 1 :

                        # Chargement des joueurs du tournoi
                        listPlayers = tournament.getplayersList()

                        # Instantiation des objets Round et Game
                        round = Round("Round",str(datetime.now()))
                        game = Game(listPlayers)

                        # Lancement de la partie 
                        tournament.startRoundsGame(round,game)
                        user_choice3_input = 0 
                user_choice_input = 0 
            elif user_choice_input == 2:

                choice4_input = [0, 1, 2, 3, 4, 5]
                user_choice4_input = Input.makeRightChoiceInput(choice4_input,INPUT.MENU_REPORTS)
               
                while user_choice4_input != 0 :     
                    if user_choice4_input == 1 :
                        Reports.displayOfAllPlayers()
                        user_choice4_input = 0
                    elif user_choice4_input == 2 :
                        Reports.displayOfAllTournaments()
                        user_choice4_input = 0
                    elif user_choice4_input == 3 :
                        Reports.displayOfTournament()
                        user_choice4_input = 0
                    elif user_choice4_input == 4 :
                        Reports.displayOfPlayersByTournament()
                        user_choice4_input = 0
                    elif user_choice4_input == 5 :
                        Reports.displayOfallRoundsgamesByTournament()
                        user_choice4_input = 0

            choice5_input = ["Y","N"]
            user_choice5_input = Input.makeRightChoiceInput(choice5_input,INPUT.STR_DISPLAY_REPORTS,False)
            if user_choice5_input == "N" :
                user_choice_input = 0
            else:
                user_choice_input = 2
               

                
             
                
         
           

                    
        Tournament.resetPlayerDb()
        Tournament.resetDbRound()               
        print(INPUT.END_GAME)  


    @staticmethod
    def createTournament(date):
        """Menu de creation des tournois"""
        tournament = None
        print(INPUT.MENU_TITLE_TOURNAMENT)  
        name = Input.makeValideChoiceInput(INPUT.STR_TOURNAMENT_NAME)     
        location = Input.makeValideChoiceInput(INPUT.STR_TOURNAMENT_LOCATION)
        numberOfRounds = Input.makeValideChoiceInput(INPUT.STR_TOURNAMENT_NUMBER_OF_ROUNDS,True)
        comment = Input.makeValideChoiceInput(INPUT.STR_TOURNAMENT_COMMENT)
        tournament = Tournament(name,location,date,numberOfRounds,comment)

        print(INPUT.STR_TOURNAMENT_SAVED)

        return tournament

    @staticmethod
    def createPlayers(tournament):
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
            tournament.addPlayer(player)
            player.save()
            print(INPUT.STR_PLAYER_SAVED)
            user_choice2_input = Input.makeRightChoiceInput(choice2_input,INPUT.STR_IF_ADD_NEW_PLAYER)   
        tournament.setPlayerList(Tournament.loadListPlayers())        
        print("Nous avons terminé de créer les joueurs")
        

    
  
 
