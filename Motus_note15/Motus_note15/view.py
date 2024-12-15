"""
Antoine ROCHAS
18/12/23
Fichier contenant les élément graphique du jeu
"""

import tkinter as tk 

import controller

class Motus(tk.Tk):
    """
    Class principale du jeu. Element graphique
    """
    def __init__(self):
        super().__init__()
        self.configure(bg="bisque")
        self.geometry("800x700")
        self.title("Motus")
        self.initUI()
        self.placeUI()
        
        self.__boxes = []
        self.__word = ""
        self.__controller = controller.Controller()
        self.__guess = ["","","","","",""]
        self.__nGuess = 0
        self.__score = 0

    def initUI(self):
        """
        Crée les éléments graphiques du jeu.
        """
        self.btnFrame = tk.Frame(self,bg="bisque")
        self.quitBtn = tk.Button(self.btnFrame,bg="white",fg="black",text="Quitter",command=self.destroy)
        self.playBtn = tk.Button(self.btnFrame,bg="white",fg="black",text="Jouer",command=self.play)
        self.scoreLabel = tk.Label(self.btnFrame,bg="bisque",text="Score : 0")
        self.indiceLabel = tk.Label(self.btnFrame,bg="bisque",text="")
        self.gameFrame = tk.Frame(self,bg="bisque")
        self.gameCanvas = tk.Canvas(self.gameFrame,width=550, height=550, highlightthickness=0,border=0,bg="bisque")
        self.entry = tk.Entry(self.gameFrame, width=25, bg="white", fg="black")
        self.guessBtn = tk.Button(self.gameFrame, text="Deviner",bg="white",fg="black",command=self.guess)

    def placeUI(self):
        """
        Méthode permettant de placer les éléments graphiques
        """
        self.btnFrame.pack(side=tk.LEFT, pady=10)
        self.quitBtn.pack(pady=10,padx=10)
        self.playBtn.pack(pady=10,padx=10)
        self.scoreLabel.pack(pady=10,padx=10)
        self.indiceLabel.pack(pady=10,padx=10)
        self.gameFrame.pack(side=tk.RIGHT,pady=10,padx=25)
        self.gameCanvas.pack(pady=25)
        self.entry.pack()
        self.guessBtn.pack(pady=10)

    def play(self):
        """
        Méthode permettant de lancer le jeu.
        """
        # Pour reset
        self.__guess = ["","","","","",""]
        self.__nGuess = 0
        self.__boxes = []

        self.__word = self.__controller.getWord()
        self.gameCanvas.delete(tk.ALL)
        print(self.__word)
        for j in range(6):
            self.__boxes.append([])
            for i in range(6):
                box = self.gameCanvas.create_rectangle(75+i*75+25,75+j*75+25,75+i*75-25,75+j*75-25,fill="bisque")
                self.__boxes[j].append(box)
        
        character = self.__word[0]
        indice = ["_","_","_","_","_","_"]
        for i,char in enumerate(self.__word):
            if char == character:
                indice[i] = character
                
        self.indiceLabel.configure(text="Indice : "+"".join(indice))
                
    def displayWord(self,currentGuess):
        """
        Méthode permettant d'afficher le mot entré
        """
        for i,char in enumerate(currentGuess):
            if char == self.__word[i]:
                self.gameCanvas.create_text(75+i*75,self.__nGuess*75+75,fill="black",text=char.upper(),font=("Calibri",30,"bold"),anchor=tk.CENTER)
                self.gameCanvas.itemconfigure(self.__boxes[self.__nGuess][i],fill="green")
                self.__guess[i] = char 
            elif self.is_yellow(char,currentGuess):
                self.gameCanvas.create_text(75+i*75,self.__nGuess*75+75,fill="black",text=char.upper(),font=("Calibri",30,"bold"),anchor=tk.CENTER)
                self.gameCanvas.itemconfigure(self.__boxes[self.__nGuess][i],fill="yellow")
            else:
                self.gameCanvas.create_text(75+i*75,self.__nGuess*75+75,fill="white",text=char.upper(),font=("Calibri",30,"bold"),anchor=tk.CENTER)
                self.gameCanvas.itemconfigure(self.__boxes[self.__nGuess][i],fill="red")
                
        self.__nGuess += 1
            
            
    def guess(self):
        """
        Méthode permettant d'essayer de deviner le mot
        """
        currentGuess = self.entry.get()
        self.entry.delete(0,tk.END)
        if len(currentGuess) != 6:
            return
        self.displayWord(currentGuess)
        if ''.join(self.__guess) == self.__word and self.__nGuess < 6:
            self.__score += 1
            self.scoreLabel.configure(text=f"Score : {self.__score}")
            return
        if self.__nGuess == 6:
            self.__score = 0
            self.scoreLabel.configure(text="Score : 0")
            
    def is_yellow(self,char,currentGuess):
        """
        Méthode permettant de déterminer si le charactère doit être en jaune
        """
        if char not in self.__word:
            return False
        
        mot = list(self.__word)
        for i,letter in enumerate(currentGuess):
            if mot[i]==letter:
                mot[i] = ""
        
        if char in mot:
            return True
        else :
            return False

            
            
            