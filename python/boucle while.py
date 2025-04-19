# Demande à l'utilisateur une liste de notes (exemple: 12, 16, 18, 6, 10) 

nombres_tab = input("Veuillez rentrer une liste de notes (séparées par virgules) : ").split(", ")

    # Convertir chaque élément de la liste créé avec split() en float

nombres_liste = [float(x) for x in nombres_tab]

    # Calcul et affichage du résultat de la moyenne des notes

resultat = 0

min = nombres_liste [0] # la note la plus basse, on suppose la première

for element in nombres_liste:

    if (element<min):   # il y a plus bas

        min = element

    resultat = resultat + element

 # on enlève la note la plus basse

moy = resultat / len(nombres_liste)

resultat -= min

moy_sans_note_basse = resultat / (len(nombres_liste) - 1)

print("Moyenne de notes : {:f}, sans la plus basse: {:f}".format(moy, moy_sans_note_basse))