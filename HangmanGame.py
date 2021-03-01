from HangmanEnglish import Word_Guesser
from HangmanLangueFrançaise import Mot_Devinateur

if __name__ == '__main__':
    Play_Again = 'yes'
    Lang_in = ['english', 'french', 'anglaise', 'francaise']
    print('HANGMAN')
    lang_input = input('What language do you want to play?\n(Type English or French)\nQuelle langue voulez-vous jouer ?\n(Tapez Anglaise ou Française)\n')
    while lang_input.lower() not in Lang_in:
        lang_input = input('Sorry. That language is not supported yet.\n(Type English or French)\n')
    while Play_Again.lower() == 'yes' or Play_Again.lower() == 'y' or Play_Again.lower() == 'oui' or Play_Again.lower() == 'o':
        if lang_input.lower() == 'english' or lang_input.lower() == 'anglaise':
            Eng_Game = Word_Guesser()
            Eng_Game.guess()
        else:
            Fr_Game = Mot_Devinateur()
            Fr_Game.guess()
        if lang_input.lower() == 'english':
            Play_Again = input('Do you want to play again?\n(Type Yes or No)\n')
        else:
            Play_Again = input('Voulez-vous rejouer ?\n(Tapez Oui ou Non)\n')


