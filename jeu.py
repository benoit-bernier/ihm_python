import util

class Jeu:
    def __init__(self, terrain, piou, score=0, arret_jeu=False, vitesse=util.VITESSE):
        """
        Initialise un objet Jeu, composé d'un terrain et d'un piou. Le score est initialisé à 0 et la vitesse à 5
        """
        self.terrain = terrain
        self.piou = piou
        self.score =  score
        self.arret_jeu = arret_jeu
        self.vitesse = vitesse
        
    def arreter_jeu(self):
        """
        Passe la propriété arret_jeu à True
        """
        self.arret_jeu = True