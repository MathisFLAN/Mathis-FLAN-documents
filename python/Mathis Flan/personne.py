from maison import Maison
from appartement import Appartement

class Personne:
    def __init__(self, nom: str, prenom: str, nombre_biens: int = 0, budjet: int = 0):
        self.nom = nom
        self.prenom = prenom
        self.nombre_biens = nombre_biens
        self.budjet = budjet
        self.biens = []

    def verif_des_biens(self, logement):
        self.nombre_biens += 1
        if self.nombre_biens > 3 :
            raise Exception("La personne", self.nom, self.prenom, "possède plus de 3 biens.")
        self.calcul(logement)

    def calcul(self, logement):
        logement.prix = 0
        prix_surface = 12
        if isinstance(logement, Maison):
            prix_surface += 2
            if logement.piscine:
                self.budjet += 100
                logement.prix += 100
        if logement.region != "Occitanie":
            prix_surface += 1
        self.budjet += prix_surface * logement.surface
        logement.prix = prix_surface * logement.surface
        self.biens.append(logement)

    def afficher_biens(self):
        for i in range(len(self.biens)):
            self.biens[i].details()