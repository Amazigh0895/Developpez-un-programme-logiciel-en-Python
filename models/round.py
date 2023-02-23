from tinydb import TinyDB,Query
from views import menuConstants as INPUT
class Round:
    """classe tour"""

    # Déclartation d'un variable static
    db = TinyDB('data/tournaments/list_rounds_games.json')
    User = Query()

    def __init__(self,name,dateTime):
        """initialisation de la partie"""
        self.__name = name
        self.__dateTime = dateTime
        self.__listGames = {}
        
    # Getters    
    def getListGames(self):
        """retourne la liste des matchs"""
        return self.__listGames
      
    def getName(self):
        return self.__name
    def getDateTime(self):
        """renvoi la l'heure et la date """
        return self.__dateTime
    # Setters
    def setListGames(self,listGames):
        """rajoute les matchs dans la liste"""
        self.__listGames = listGames
    def setName(self,name):
        self.__name = name

    def startGame(self,obj_game):
        """declenche la partie et renvoie une liste de resultat dans un tableau gameResults
        prend en parametre une liste de pairs de jouerus     
        
        """
        
        collectionOfPaires=obj_game.pair()

        indexMax=len(collectionOfPaires)
        player1 = []
        player2 = []
        resultatplayer1 = []
        resultatplayer2 = []
       
        gameResults_dict = {"game":'',"player":'',"results":'',"score":''}
       
        
        for i in range(indexMax):
            nbmatch  =f"match {i+1}"
            print(nbmatch)
            player1.append(collectionOfPaires[i][0])
            player2.append(collectionOfPaires[i][1])

            
            print(f"""
                      {player1[i].lastName} | contre | {player2[i].lastName}         
                      quel est le resultat:
                            |tapez 1 pour {player1[i].lastName} gagant 
                            |tapez 2 pour {player2[i].lastName} gagant
            -------------------------------------------------------------     
            """)
            choice_results_input = [1 , 2]
            user_choice_results_input = ""
            while user_choice_results_input not in choice_results_input:
                try:
                    user_choice_results_input = int(input(INPUT.STR_INPUT_RESULTS_GAME))
                except:
                    print(INPUT.ERROR_VALUE_INPUT)
            
            if (user_choice_results_input == 1):
                player1[i].setScore(1)
                player2[i].setScore(0)
                resultatplayer1 = f"{player1[i].lastName} gagne contre {player2[i].lastName}"
                resultatplayer2 = f"{player2[i].lastName} perd contre {player1[i].lastName}"

            elif (user_choice_results_input == 2 ):
                player1[i].setScore(0)
                player2[i].setScore(1)
                resultatplayer1 = f"{player1[i].lastName} perd contre {player2[i].lastName}"
                resultatplayer2 = f"{player2[i].lastName} gagne contre {player1[i].lastName}"

            gameResults_dict["game"] = nbmatch
            gameResults_dict["player"] = player2[i].lastName
            gameResults_dict["results"] = resultatplayer2
            gameResults_dict["score"] = player2[i].getScore()
            gameResults_dict["player"] = player1[i].lastName
            gameResults_dict["results"] = resultatplayer1
            gameResults_dict["score"] = player1[i].getScore()
            round_dict = {"name":f'{self.getName()}',"dateTime":f'{self.getDateTime()}',"game":f'{gameResults_dict}'}
            self.setListGames(round_dict)
            self.save()
                  
    def reclassify(self,listPlayers):
        """reclasse la liste des joueurs en fonction de leur score"""

        indexMax = len(listPlayers)
        cassificationOfPlayersByScore = []

        scoreMinimum = 0
        scoreMaximum = 1
        for i in range(indexMax):

            if(listPlayers[i].getScore() >scoreMinimum ):
                cassificationOfPlayersByScore.append(listPlayers[i])

        for i in range(indexMax):
            if(listPlayers[i].getScore() < scoreMaximum ):
                cassificationOfPlayersByScore.append(listPlayers[i])

        return cassificationOfPlayersByScore
                     
    def save(self):
        """sauvegarde la liste des matchs des tours dans la base de donnée json"""
        Round.db.insert(self.__dict__)

    @staticmethod
    def load():
        """charge les données des matchs depuis le fichier json"""
        listRound_game_dict = Round.db.all()
        return listRound_game_dict
        
        
       

                
   

