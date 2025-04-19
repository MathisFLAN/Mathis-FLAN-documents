from random import randint

identité = {"prenom", "nom", "age"}

identité["prenom"] = input("quel est le prénom de cette personne ?")
identité["nom"] = input("quel est son nom ?")
identité["age"] = randint(0, 100)

categories = ("junior", "adult", "senior")

if identité["age"] < 18 :
    cat = 0
elif identité["age"] < 65 :
    cat = 1
else :
    cat = 2

print("la personne d'identité :", identité, "est de la catégorie des", categories[cat])