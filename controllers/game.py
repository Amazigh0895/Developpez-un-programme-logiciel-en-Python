class Game:
    """la classe match"""
    def __init__(self, listPlayers):
        """initialisation de la variable pairesOfPlayers qui recoit
          un tableau de pairs de joueurs"""

        self.__listPlayers = listPlayers

    def getListPlayers(self):
        """retourne la liste des joueurs"""
        return self.__listPlayers

    def pair(self):
        """retourne une liste de pairs de joueurs"""

        collectionOfPaires = []

        indexMax = len(self.__listPlayers)
        indexOfI = 0
        indexOfY = (indexMax/2)

        i = int(indexOfI)
        y = int(indexOfY)

        for i in range(i, indexMax):
            for y in range(y, indexMax):
                if (i == y):
                    pass
                else:
                    collectionOfPaires.append([self.__listPlayers[i],
                                               self.__listPlayers[y]])
                if (i < indexMax and y < indexMax):
                    i = i+1
                    y = y+1
        return collectionOfPaires
