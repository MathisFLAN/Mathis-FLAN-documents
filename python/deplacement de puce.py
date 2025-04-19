from random import randint

#initialisations de la classe "Puce"
class Puce :
    def __init__ (self):
        self.x = 0
        self.y = 0
        self.direction1 = ""
        self.direction2 = ""

    # cette définitions va ajouter les différents déplacements exécuter aux coordonnées de la puce.
    def deplacer (self, ajoutx, ajouty, nombre):
        self.x += ajoutx
        self.y += ajouty
        print("déplacement", nombre, ":", self.x, ",", self.y)

    #def dirifer vas définir la positions de la puce par rapport au centre 0, 0.
    def diriger (self, x, y, direction1, direction2):
        #Est ou Ouest
        if (x > 0):
            self.direction1 = "E"
        elif (x < 0):
            self.direction1 = "O"
        else :
            self.direction1 = ""
        #Nord ou Sud
        if (y > 0):
            self.direction2 = "N"
        elif (y < 0):
            self.direction2 = "S"
        else :
            self.direction2 = ""

#début du programme principal
p=Puce()
print("le centre a pour coordonnées : 0, 0")

#défintions des 3 déplacements de la puce.
boucle = 1
while boucle != 4:
    p.deplacer (randint(-10, 10), randint(-10, 10), boucle)
    boucle += 1

#vérification de la position de la puce.
p.diriger (p.x, p.y, p.direction1, p.direction2)

#phrases réponses + calcul de la distance entre la puce et le centre.
print("la puce se trouve donc au", p.direction2, ",", p.direction1, "par rapport au centre.")
distance = (0 - p.x)*2 + (0 - p.y)*2
print("Et la puce se trouvent à une distance égale à :", distance)