from random import randint

class LesMots:
    def __init__(self):
        self.Mots = ['maison', 'ville', 'porte', 'route', 'homme', 'femme', 'amour', 'voiture', 'temps', 'bien', 'fois', 'rue', 'monde', 'tête', 'temps', 'pays', 'raison', 'cœur', 'dieu', 'monde', 'jour', 'monsieur', 'personne', 'part', 'chambre', 'être', 'avoir', 'pouvoir', 'faire', 'mettre', 'dire', 'devoir', 'prendre', 'donner', 'aller', 'vouloir', 'savoir', 'falloir', 'voir', 'demander', 'trouver', 'rendre', 'venir', 'passer', 'comprendre', 'rester', 'tenir', 'porter', 'parler', 'montrer', 'lent', 'rapide', 'méchant', 'belle', 'intelligent', 'ancien', 'nouveau', 'triste', 'heureux', 'Adorable', 'Timide', 'bon', 'Sage', 'fort', 'magnifique', 'merveilleux', 'brave', 'Dynamique', 'élégant', 'énervé', 'Sombre', 'Mauvais', 'Possible', 'Moyen', 'Fatigant', 'Rapidement', 'Malheureusement', 'Lentement', 'Couramment', 'Egalement', 'Parfois', 'encore', 'tellement', 'certainement', 'probablement', 'précisément', 'beaucoup', 'souvent', 'presque', 'bientôt', 'cependant', 'désormais', 'davantage', 'Vraiment', 'habituellement', 'régulièrement', 'calmement', 'tranquillement', 'jamais', 'partout']
    def _Générer_Mot(self):
        self.num = randint(1, 100)
        self.Mot = self.Mots[self.num]
        return self.Mot