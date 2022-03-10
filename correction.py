# chaque joueur a un pseudo
# chaque joueur ne conserve qu'un seul score par chanson
# il y a 5 chanson (id 0 a 4)
# le pire score possible = 50/100, 0 = chanson non jouer
# on peut calculer la moyennes de ses scores enregistré
# on peut calculer son score total
# on peut afficher le num de la chanson qui possède le meilleur score
# on peut afficher le num de la chanson qui possède le pire score
# on peut afficher ses scores
# on peut ajouter un score 

#Partie A


from typing_extensions import Self

from main import Player


class player:
    def __init__(self, name):
        self.__pseudo = name
        self.__score = {0:0, 1:0, 2:0, 3:0, 4:0} #peut s'afficher [0,0,0,0,0]

    def ajouteScore(self, num, valeur):
        if (self.__score[num] < valeur):
            self.__score = valeur
    
    def afficheScore(self):
        print (self.__score)
    
    def getChansonPireScore(self):
        pireScore = 50
        pireScoreIndex = 0
        total = 0
        for i in range(5):
            if (self.__score[i] < pireScore):
                total += self.__score[i]
                pireScore=self.__score[i]
                pireScoreIndex = i
        if (total==0):
            pireScoreIndex = -1
        return pireScoreIndex

    def getChansonBestScore(self):
        bestScore = 50
        bestScoreIndex = -1
        total = 0
        for i in range(5):
            if (self.__score[i] > bestScore):
                total += self.__score[i]
                bestScore=self.__score[i]
                bestScoreIndex = i
        return bestScoreIndex

    def calculeScoreTotal(self):
        total = 0
        for i in range (5):
            total+=self.__score[i]
        return total
    
    def calculeMoyenneScores(self):
        nbrChansonJouees=0
        for i in range(5):
            if (self.__score[i]>=50):
                nbrChansonJouees+= 1
        return self.calculeScoreTotal()/nbrChansonJouees
    def getScore():
        return self.__score


#Partie B

#un karaoke possede un certain nbr de chansons
# un karaoke possede un ou plusieurs players
# chaque chanson a un nom en toutes lettre
#on peut ajouter ou supprimé un player
# on peut visualiser le meilleur score pour une chanson
# on peut visualiser le player avec le meilleur score 
#on peut connaitre le meilleur score toutes chansons confondu
# on peut connaitre la meilleure moyenne

class Karaoke:
    def __init__(self,pseudo1erjoueur):
        self.__chanson={
            0:"Highway to hell",
            1:"Bohemian Rhapsody",
            2:"We will rock you"
        }
        self.__listePlayers={pseudo1erjoueur:Player(pseudo1erjoueur)}
    def getMeilleureMoyenne(self):
        bestAverage =0
        for joueur in self.__listePlayers:
            if(joueur.calculeMoyenneScores()>bestAverage):
                bestAverage=joueur.calculeMoyenneScores()
        return bestAverage
    def getBestScoreAllSongs(self):
        bestScore=0
        for joueur in self.__listePlayers:
            if(joueur.getScore(joueur.getChansonBestScore())>bestScore):
                bestScore=joueur.getScore(joueur.getChansonBestScore())
        return bestScore
    def getBestPlayerTotal(self):
        bestScore=0
        for joueur in self.__listePlayers:
            if(joueur.calculeScoreTotal())>bestScore:
                bestScore=joueur.calculeScoreTotal()
        return bestScore
    def getBestScoreForASong(self,numChanson):
        bestScore=0
        for joueur in self.__listePlayers:
            if(joueur.getScore(numChanson)>bestScore):
                bestScore=joueur.getScore(numChanson)
        return bestScore
    def addPlayer(self,pseudo):
        self.__listePlayers[pseudo]=Player(pseudo)
    def delPlayer(self,pseudo):
        self.__listePlayers.pop(pseudo)