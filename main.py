from voitures import Voiture

v = Voiture("Toyota", "Corolla", 2020, 20000)
v.afficher_voiture()

from crud_db import connecter_db

conn = connecter_db()
print("connexion OKEY")
conn.close()

from crud_db import ajouter_voiture

v = Voiture("BMW", "M3CS", 2022, 80000)
ajouter_voiture(v)