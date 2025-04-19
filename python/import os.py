import os

print(os.remove("C:/Users/mathi/Documents/python/renome.txt")) #supprimé un fichier

print(os.rename("C:/Users/mathi/Documents/python/tax.txt", "C:/Users/mathi/Documents/python/renome.txt")) #renomé un fichier f1 en f2

print(os.path.isfile("C:/Users/mathi/Documents/python/tax.txt")) #cherché l'existance d'un fichier
print(os.path.isfile("f"))

print(os.stat("C:/Users/mathi/Documents/python/tax.txt")) #fournit des infos sur le fichiers