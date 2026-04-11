from voitures import Voiture
from crud_db import ajouter_voiture, supprimer_voiture, connecter_db


v1 = Voiture("Toyota", "Corolla", 2020, 20000)
ajouter_voiture(v1)

print("Ajout OK")


conn = connecter_db()
print("Connexion OK")
conn.close()


v2 = Voiture("BMW", "M3CS", 2022, 80000)
ajouter_voiture(v2)


supprimer_voiture(1)
print("Suppression OK")

from crud_db import recuperer_voitures

voitures = recuperer_voitures()

print(f"Liste des voitures :")
for v in voitures:
    v.afficher_voiture()