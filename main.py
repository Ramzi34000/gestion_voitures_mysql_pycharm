from voitures import Voiture
from crud_db import ajouter_voiture, supprimer_voiture, connecter_db, recuperer_voitures, modifier_voiture


v1 = Voiture("Toyota", "Corolla", 2020, 20000)
ajouter_voiture(v1)
print("Ajout OK")


conn = connecter_db()
print("Connexion OK")
conn.close()



v2 = Voiture("BMW", "M3CS", 2022, 80000)
ajouter_voiture(v2)



v_mod = Voiture("Toyota", "Corolla Sport", 2021, 22000, 1)
modifier_voiture(v_mod)
print("Modification OK")



supprimer_voiture(2)
print("Suppression OK")



voitures = recuperer_voitures()

print(f"Liste des voitures :")
for v in voitures:
    v.afficher_voiture()