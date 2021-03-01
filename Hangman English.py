from WordStorage import Word_Generator
from HangmanFig import HangmanFigure


class Word_Guesser: 
    def __init__(self): 
        self.generate = Word_Generator()
        self.figure = HangmanFigure()
        self.word = self.generate._Generate_Word()
        self.meaning = self.generate._Generate_Meaning()
    def guess(self):
        self.guessed = []
        self.print_guessed()
        print('Meaning: ' + str(self.meaning))
        num = 0
        while num < 7:
            print(num)
            self.ltr = input('Guess a letter: ')
            contains_digit = any(map(str.isdigit, self.ltr))
            while len(self.ltr) > 1 or contains_digit == True:
                self.ltr = input('Only a one letter: ')
                contains_digit = any(map(str.isdigit, self.ltr))
            self.guessed.append(self.ltr)
            if self.ltr not in self.word:
                print(self.figure.Return_Fig(num))
                num += 1
            self.print_guessed()
            if '_' not in self.det:
                print('Congratulations! You\'ve guessed the word.')
                break
        if num == 7:
            print('Game Over! It\'s ' + str(self.word))
    def print_guessed(self):
        self.det = ' '.join(c if c in self.guessed else '_' for c in self.word)
        print(self.det)
