from random import randint

class Controller:
    """
    Controller du jeu
    """
    def __init__(self):
        self.__path = "mot.txt"
        
    def getWord(self):
        """
        Retourne un mot choisi au hasard
        """
        with open(self.__path,"r") as file:
            words = file.readlines()
        
        index = randint(0,len(words)-1)
        return words[index].replace("\n","")