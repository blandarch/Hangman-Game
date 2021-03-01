from WordStorage import Word_Dictionary
from HangmanFig import HangmanFigure


class Word_Guesser: 
    def __init__(self): 
        self.generate = Word_Dictionary()
        self.figure = HangmanFigure()
        self.word = self.generate.Word()
        self.meaning = self.generate.Meaning()
    def guess(self):
        self.guessed = []
        self.print_guessed()
        print('Meaning:')
        self.generate.Print_Meaning()
        num = 0
        while num < 7:
            print(num)
            self.ltr = input('Guess a letter/Guess the word: ')
            contains_digit = any(map(str.isdigit, self.ltr))
            if contains_digit == True:
                self.ltr = input('That is a number! (Put a letter): ')
                contains_digit = any(map(str.isdigit, self.ltr))
            elif len(self.ltr) > 1 and contains_digit == False:
                if self.ltr.lower() == self.word:
                    print('Congratulations! You\'ve guessed the word.')
                    break
            elif len(self.ltr) > 1:
                self.ltr = input('Only one letter: ')
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