from random import randint

#version avec "input"
#initialisation des listes d'appareil et client

liste_appareil = {
    "REDMI 14": {"ref": "00456", "nom": "REDMI 14","marque": "XIAOMI", "prix": 300, "categ": "Android"},
    "GALAXY A54": {"ref": "00789", "nom": "GALAXY A54","marque": "SAMSUNG", "prix": 450, "categ": "Android"},
    "PIXEL 7A": {"ref": "00234", "nom": "PIXEL 7A","marque": "GOOGLE", "prix": 500, "categ": "Android"},
    "IPHONE 13": {"ref": "00567", "nom": "IPHONE 13","marque": "APPLE", "prix": 800, "categ": "Android"},
    "IPHONE 14 PRO": {"ref": "00981", "nom": "IPHONE 14 PRO","marque": "APPLE", "prix": 1200, "categ": "Android"},
    "IPHONE SE": {"ref": "00321", "nom": "IPHONE SE","marque": "APPLE", "prix": 450, "categ": "Android"}
}

liste_client = {
    "Paul": {"nom": "Paul", "prenom": "Durant", "adresse": "paul@gmail.com"},
    "Rolex": {"nom": "Rolex", "prenom": "Rousseau","adresse": "Rolex@gmail.com"},
    "Ethan": {"nom": "Ethan", "prenom": "Bertin","adresse": "Ethan@gmail.com"}
}

position = 0
prix = 0
commande = []
nombreDA = []
commande_finale = []
client = liste_client[randint(1,3)]
nombre_app = int(input("combien d'articles coulez vous ? "))

for h in range (nombre_app):
    article = input("que voulez vous commenndez ? ")
    nombre = int(input("combien en voulez vous ? "))
    for i, liste_appareil in liste_appareil.items():
        if liste_appareil["nom"] == article :
            commande_finale.append(liste_appareil["nom"])
            prix = prix + nombre*liste_appareil["prix"]
            position = position + 1
            nombreDA.append(nombre)

#initialisation des frais de commande et du prix finale de la commande
frais = 10
if prix > 999 :
    frais = 1000
prix = prix + frais

print(client["nom"], client["prenom"],"a commandé le 22/02/2025")
for j in range(len(commande_finale)):
    print(commande_finale[j])