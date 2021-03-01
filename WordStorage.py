import requests
import random
import re
from PyDictionary import PyDictionary

class Word_Dictionary:
    def load_words(self):
        with open('/Users/danskewers/english-words/words_alpha.txt') as word_file:
            self._valid_words = random.sample(set(word_file.read().split()), 1)
        return self._valid_words[0]

    def Word(self):
        self.random_word = self.load_words()
        return self.random_word

    def Meaning(self):
        self.dictionary = PyDictionary()
        self.output = self.dictionary.meaning(self.random_word, disable_errors=True)
        while self.output == None:
            self.Word()
            self.output = self.dictionary.meaning(self.random_word, disable_errors=True)
        return self.output
    
    def Print_Meaning(self):
        for key in self.output:
            print(str(key) + ': ' + str(self.output[key][0]))
    





