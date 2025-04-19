class Citron :
    forme = " ellipsoïde" 
    saveur = " acide " 
    def __init__ (self, couleur ="jaune", taille ="standard"):
        self.couleur = couleur 
        self.taille = taille 
        self.masse = 0
    def augmente_masse (self, valeur):
        self.masse += valeur
c=Citron()
print (" Attributs de classe :", c.forme , c.saveur )
print (" Attributs d' instance :", c.taille , c.couleur)
c.augmente_masse (100)
print(c.masse)