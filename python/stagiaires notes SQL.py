import sqlite3
import os

#initialisation du fichier.
conn = sqlite3.connect('stagiaires_notes.db')
cur = conn.cursor()

#création de la table
cur.execute("DROP TABLE stagiaires")
cur.execute("DROP TABLE notes")
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS 
    stagiaires(id INT, nom TEXT, prenom TEXT)
    """)
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS 
    notes(id INT, note INT, id_stagiaire)
    """)

#Maintenant, on peut ajouter plusieurs stagiaires ainsi que leur notes.
cur.execute(
    """
    INSERT OR IGNORE INTO 
    stagiaires(id, nom, prenom) VALUES (1, 'Bertin', 'Ethan')
    """)
cur.execute(
    """
    INSERT OR IGNORE INTO 
    stagiaires(id, nom, prenom) VALUES (2, 'FLAN', 'Mathis')
    """)

cur.execute(
    """
    INSERT OR IGNORE INTO 
    notes(id, note, id_stagiaire) VALUES (1, 18, 1)
    """)
cur.execute(
    """
    INSERT OR IGNORE INTO 
    notes(id, note, id_stagiaire) VALUES (2, 19, 2)
    """)

#Maintenant on valide
conn.commit()
cur.close()

#Enfin, nous ajoutons les commandes pour voir si tout est correcte.
cur = conn.cursor()

#Pour la stagiaires
cur.execute('SELECT * FROM stagiaires')
liste = cur.fetchall()
print("stagiaires : ", liste)

#Pour les notes
cur.execute('SELECT * FROM notes')
liste = cur.fetchall()
print("notes : ", liste)

conn.close()

print(os.path.dirname(__file__))