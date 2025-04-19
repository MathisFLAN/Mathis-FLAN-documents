#d'abord on définit les variables

age = int(input("Quel age a le tennis man ? "))
cours = int(input("combien de cours par semaine ? "))

#définissons maintenant nos conditions17

if age < 16 :
    prix = 33 * cours
else :
    prix = 36 * cours

if cours > 3 :
    prix = prix * 0.90
elif cours > 5 : 
    prix = prix * 0.85
else :
    prix = prix

print("Vous aurez donc", cours, "par semaine, cela vous coutera donc", prix)