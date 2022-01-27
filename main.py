from unicodedata import name
from xml.dom import NoModificationAllowedErr


class Player :
    #contructeur : (_init_)
    def __init__(self, name, chanson, scoreMax, scoreJoueur) :
        self.name = name
        self.chanson = chanson
        self.__listeChanson = {0 : "chanson1", 1 : "chanson 2", 2 : "chanson 3", 3 : "chanson 4", 4: "chanson 5"}
        self.scoreMax = scoreMax
        self.__scoreJoueur = scoreJoueur

        
    def getname(self,):
        return self.name

    def getlistechanson(self, listeChanson):
        listeChanson = {0 : "chanson1", 1 : "chanson 2", 2 : "chanson 3", 3 : "chanson 4", 4: "chanson 5"}
        for i in range(len(listeChanson)):
            if(i == self.__listeChanson):
                self.__listeChanson = listeChanson[i]
        return self.__listeChanson


    def getscoreJoueur (self):
        listescore = {0 : 0, 1 : 50, 2 : 60, 3 : 70, 4: 80, 5: 90, 6: 100}
        for i in range(len(listescore)):
            if (i == self.__listeChanson):
                self.scoreJoueur = listescore[i]
        return self.scoreJoueur
       
        
    def getscoreMax (self):
        scoreMax = {0 : 0, 1: 70, 2: 80, 3: 60, 4: 90}
        for i in range (len(scoreMax)):
            if (i == self.__listeChanson):
                self.scoreMax = scoreMax[i]
            return self.scoreMax
    
        
joueur_1 = Player("Marley", 0,0,0)

print(joueur_1)


class Karaoke:
    def __init__(self, name, chanson, scoreMax, scoreJoueur) :
        self.nomJoueur = name
        self.chanson = chanson



#programme principale

int(input("Bienvenue a votre nouveau Karaoké en ligne,"))
