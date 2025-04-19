liste_departements = {
    31: {"Département": "Haute Garonne", "ChefLieu": "Toulouse", "Habitants": 1.5},
    32: {"Département": "Gers", "ChefLieu": "Auch", "Habitants": 0.8},
    75: {"Département": "Ile de France", "ChefLieu": "Paris", "Habitants": 1.4},
    29: {"Département": "Finistère", "ChefLieu": "Quinper", "Habitants": 1.2}
}

numerodepartement = int(input("saisissez un numéro de département : "))
print(f"voici les infos du département choisi : {liste_departements[numerodepartement]}")

max = 0
for i, liste_departements in liste_departements.items():
    if liste_departements["Habitants"] > max :
        max = liste_departements["Habitants"]
        dept_pop = liste_departements["Département"]

print(f"Most populated dept: {dept_pop}")