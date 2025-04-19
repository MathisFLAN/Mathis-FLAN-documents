import sqlite3

#initialisation du fichier.
conn = sqlite3.connect('Garage.db')
cur = conn.cursor()

#création de la table
cur.execute("DROP TABLE parking")
cur.execute(
    "CREATE TABLE IF NOT EXISTS parking(id INT, etat TEXT CHECK(etat IN ('libre', 'occupe')), voiture TEXT)")

#ajout des données (on commence qu'avec des places vides)
for i in range(1, 51) :
    sql=f"INSERT INTO parking(id, etat, voiture) VALUES ({i}, 'libre', 'aucune')"
    cur.execute(sql)

#Maintenant, on peut ajouter des places occupé en modifiant certaines places libres (peu importe).
cur.execute(
    "UPDATE parking SET etat='occupe', voiture = 'Porsche' where id = 1")
cur.execute(
    "UPDATE parking SET etat='occupe', voiture = 'Audi' where id = 2")
cur.execute(
    "UPDATE parking SET etat='occupe', voiture = 'Mercedes' where id = 7")

#Maintenant on valide
conn.commit()
cur.close()

#Enfin, nous ajoutons les commandes pour voir si tout est correcte.
cur = conn.cursor()
cur.execute('SELECT * FROM parking')

liste = cur.fetchall()
print(liste)
conn.close()