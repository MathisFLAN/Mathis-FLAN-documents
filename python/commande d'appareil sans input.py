from random import randint
from datetime import datetime #à savoir comment l'utiliser

    #initialisation des listes d'appareil et client :

liste_appareil = {
    "REDMI 14": {"ref": "00456", "nom": "REDMI 14","marque": "XIAOMI", "prix": 300, "categ": "Android"},
    "GALAXY A54": {"ref": "00789", "nom": "GALAXY A54","marque": "SAMSUNG", "prix": 450, "categ": "Android"},
    "PIXEL 7A": {"ref": "00234", "nom": "PIXEL 7A","marque": "GOOGLE", "prix": 500, "categ": "Android"},
    "IPHONE 13": {"ref": "00567", "nom": "IPHONE 13","marque": "APPLE", "prix": 800, "categ": "Android"},
    "IPHONE 14 PRO": {"ref": "00981", "nom": "IPHONE 14 PRO","marque": "APPLE", "prix": 1200, "categ": "Android"},
    "IPHONE SE": {"ref": "00321", "nom": "IPHONE SE","marque": "APPLE", "prix": 450, "categ": "Android"}
}

liste_client = {
    1: {"nom": "Paul", "prenom": "Durant", "adresse": "paul@gmail.com"},
    2: {"nom": "Rolex", "prenom": "Rousseau","adresse": "Rolex@gmail.com"},
    3: {"nom": "Ethan", "prenom": "Bertin","adresse": "Ethan@gmail.com"}
}

    #initialisation des différents calculs :

client = liste_client[randint(1,3)]

def acheter(appareil1, appareil2):
    A1 = liste_appareil[appareil1]
    A2 = liste_appareil[appareil2]

    prix1 = 1 * A1["prix"]
    prix2 = 2 * A2["prix"]

        #initialisation des frais de transports :

    prixF = prix2 + prix1
    transport = 0
    if prixF < 1000:
        transport = 10
        prixF = prixF + transport

        #Ci dessous, voici le programme permettant d'afficher toute les informations de la commande :

    print(client["nom"], client["prenom"],"a passé une commandé :")
    print("article :", A1["nom"], "nombre : 1   prix :",prix1, "€")
    print("article :", A2["nom"], "nombre : 2   prix :",prix2, "€")
    print("transport :", transport, "€")
    print("prix total :", prixF, "€")


    #saisir les appareils à commander ici
acheter("IPHONE 14 PRO", "PIXEL 7A")