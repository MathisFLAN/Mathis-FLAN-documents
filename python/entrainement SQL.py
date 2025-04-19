import sqlite3

# 1) se connecter, créer la base géographique
conn = sqlite3.connect('dBGeo.db')

#créer le curseur
cur = conn.cursor()

#créer la table pays
cur.execute(
    "CREATE TABLE IF NOT EXISTS pays(id INT, nom TEXT, population INT)")

#insérer 2 pays
cur.execute(
    "INSERT INTO pays(id, nom, population) VALUES(1,'france', 67)")
cur.execute(
    "INSERT INTO pays(id, nom, population) VALUES(2,'Espagne', 30)")

#valiser/fermer
conn.commit()
cur.close()

# 2) lire ensuite
cur = conn.cursor()
cur.execute('SELECT * FROM pays')

liste = cur.fetchall()
print(liste)
conn.close()