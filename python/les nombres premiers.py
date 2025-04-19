#initialisation du nombre à choisir et du tableau.

nombreChoisi = int(input("choisissez un nombre : "))
i = 1
tabdiviseur = []

#Si dessous, c'est la boucle pour vérifier si oui ou non les nombre entre 0 et le nombre choisi sont des diviseurs de celui ci.
#Et au lieu de while et i, on aurait pu faire : for i in range(1, nombrechoisi.)

while i != nombreChoisi + 1 :
    if nombreChoisi % i == 0 :
        tabdiviseur.append(i)
    i = i + 1

#Si les seuls diviseurs sont 1 et le chiffre choisis lui même, alors c'est un nombre premier, sinon on affiche tous les autres diviseurs.

if tabdiviseur[0] == 1 and tabdiviseur[1] == nombreChoisi :
    print("c'est un nombre premier")
else :
    print("les diviseurs de ce nombre sont donc : ", tabdiviseur)