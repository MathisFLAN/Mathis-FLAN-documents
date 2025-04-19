#

phrase = input("choissez votre phrase : ")

#

dictionnaire = {"MAJUSCULE": 0, "minuscule": 0, "mots":1, "autres": 0}

#

mots = []
retenu = 0

#initialisation de la boucle en fonction du nombre de lettre dans la phrase écrite

for i in phrase :
    if i.isupper() :
        dictionnaire["MAJUSCULE"] += 1
        retenu += 1
    elif i.islower() :
        dictionnaire["minuscule"] += 1
        retenu += 1
    elif i.isspace() :
        dictionnaire["mots"] += 1
        mots.append(retenu)
        retenu = 0
    else :
        dictionnaire["autres"] += 1

#derniere phrase :

print("Dans cette phrase, il y a", dictionnaire ["MAJUSCULE"], "majuscules,", dictionnaire ["minuscule"], "minuscule, et surtout", dictionnaire ["mots"], "mots de", mots, "lettres, et enfin", dictionnaire ["autres"], "autres caractères.")