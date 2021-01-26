import util

class Jeu:
    """
    Classe représentant le jeu
    ... 
    Attributs :        
    ----------
    terrain : 
        Défini le terrain du jeu 
    piou : 
        Défini le personnage du jeu
    score :
        Score atteint dans le jeu
    arret_jeu :
        booleen indiquant que le jeu est arrêté
    vitesse : 
        vitesse de défilement du jeu
    
    
    Méthodes 
    ----
    arreter_jeu():
        Passe le booleen arret_jeu à true, arrête le jeu

    auteur : Benoit
    """
    def __init__(self, terrain, piou, score=0, arret_jeu=False, vitesse=util.VITESSE):
        """
        Initialise un objet Jeu, composé d'un terrain et d'un piou. Le score est initialisé à 0 et la vitesse à 5
        ... 
        Paramètres :        
        ----------
        terrain : Terrain
            Défini le terrain du jeu 
        piou : Piou
            Défini le personnage du jeu
        score : int
            Score atteint dans le jeu
        arret_jeu : bool
            booleen indiquant que le jeu est arrêté
        vitesse : int
            vitesse de défilement du jeu

        auteur : Benoit
        """
        self.terrain = terrain
        self.piou = piou
        self.score =  score
        self.arret_jeu = arret_jeu
        self.vitesse = vitesse
        
    def arreter_jeu(self):
        """
        Passe la propriété arret_jeu à True

        auteur : Benoît
        """
        self.arret_jeu = True