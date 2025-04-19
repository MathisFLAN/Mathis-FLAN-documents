nombreChoisi = int(input("choisissez un nombre : "))
i = 1
tabdiviseur = []
while i != nombreChoisi + 1 :
    if nombreChoisi % i == 0 :
        tabdiviseur.append(i)
    i = i + 1

if tabdiviseur[0] == 1 and tabdiviseur[1] == nombreChoisi :
    print("c'est un nombre premier")
else :
    print("les diviseurs de ce nombre sont donc : ", tabdiviseur)