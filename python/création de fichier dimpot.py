from random import randint

#initialisation des dictionnaires de données.

Personnes = {
    1: {"nom": "Paul", "impots": 3567, "nbenfant": 3},
    2: {"nom": "Mathis", "impots": 45545, "nbenfant": 1},
    3: {"nom": "Olex", "impots": 8787, "nbenfant": 0},
    4: {"nom": "Ethan", "impots": 12345, "nbenfant": 2},
    5: {"nom": "Adam", "impots": 40000, "nbenfant": 2},
    6: {"nom": "David", "impots": 25000, "nbenfant": 3},
    7: {"nom": "Personne", "impots": 0, "nbenfant": 4}
}

#choix aléatoire d'une des personnes du dictionnaire + exemple d'affichage pour tax.txt.

choix = Personnes[randint(1, 7)]
print (choix["nom"], "doit payer", choix["impots"], "€, cette personne a", choix["nbenfant"],"enfant(s)")

#création du fichier tax.txt.

revenu="C:/Users/mathi/Documents/python/tax.txt"
with open(revenu, 'wt') as fd:
    fd.write(f"{choix['nom']} doit payer, {choix['impots']} €, cette personne a {choix['nbenfant']} enfant(s)\n")
    fd.write(f"Ce fichier est en lien avec le programme création de fichier dimpot dans le dossier python\n")

#Pour être sur de savoir qu'est ce qu'il y a d'écrit dans le document tax.txt.

with open(revenu) as fd:
    print(fd.readline())