from ParolesFrançaise import LesMots
from HangmanFig import HangmanFigure


class Mot_Devinateur: 
    def __init__(self): 
        self.generate = LesMots()
        self.figure = HangmanFigure()
        self.word = self.generate._Générer_Mot()
    def guess(self):
        self.guessed = []
        self.print_guessed()
        print('Meaning: ')
        num = 0
        while num < 7:
            print(num)
            self.ltr = input('Devinez une lettre: ')
            contains_digit = any(map(str.isdigit, self.ltr))
            while len(self.ltr) > 1 or contains_digit == True:
                self.ltr = input('Seulement une lettre: ')
                contains_digit = any(map(str.isdigit, self.ltr))
            self.guessed.append(self.ltr)
            if self.ltr not in self.word:
                print(self.figure.Return_Fig(num))
                num += 1
            self.print_guessed()
            if '_' not in self.det:
                print('Félicitations! Vous avez deviné le mot.')
                break
        if num == 7:
            print('Jeu terminé! Le mot c\'est ' + str(self.word))
    def print_guessed(self):
        self.det = ' '.join(c if c in self.guessed else '_' for c in self.word)
        print(self.det)