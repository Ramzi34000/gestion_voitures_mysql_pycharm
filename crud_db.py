import mysql.connector
import json

def connecter_db():
    with open("config.json") as f:
        config = json.load(f)

    conn = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

    return conn

def ajouter_voiture(voiture):
    conn = connecter_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voiture (
        id INT AUTO_INCREMENT PRIMARY KEY,
        marque VARCHAR(50),
        modele VARCHAR(50),
        annee INT,
        prix DECIMAL(10,2)
    )
    """)

    cursor.execute(
        "INSERT INTO voiture (marque, modele, annee, prix) VALUES (%s, %s, %s, %s)",
        (voiture.marque, voiture.modele, voiture.annee, voiture.prix)
    )

    conn.commit()
    conn.close()


def supprimer_voiture(id):
    conn = connecter_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM voiture WHERE id = %s", (id,))

    conn.commit()
    conn.close()

from voitures import Voiture

def recuperer_voitures():
    conn = connecter_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM voiture")
    resultats = cursor.fetchall()

    voitures = []
    for row in resultats:
        v = Voiture(row[1], row[2], row[3], row[4], row[0])
        voitures.append(v)

    conn.close()
    return voitures


