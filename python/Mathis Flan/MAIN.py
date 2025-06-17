from personne import Personne
from appartement import Appartement
from maison import Maison

P1 = Personne("Flan", "Mathis")
P2 = Personne("Mystere", "Martin")

A1 = Appartement("Occitanie", "Toulouse", 280, 5)
A2 = Appartement("Ile de France", "Paris", 144, 2)
A3 = Appartement("Occitanie", "Carcassonne", 100, 3)

M1 = Maison("Nord-Pas-de-Calais", "Lille", 540, True)
M2 = Maison("Occitanie", "Toulouse", 1000, True)
M3 = Maison("Occitanie", "Toulouse", 432, False)

try:
    P1.verif_des_biens(M1)
    P1.verif_des_biens(A1)
except Exception as e:
    print("Impossible de faire les calculs,", e)
else:
    print("achats de", P1.nom, P1.prenom)
    P1.afficher_biens()
    print("budjet :", P1.budjet)