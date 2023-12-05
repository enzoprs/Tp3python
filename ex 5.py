debut = int(input("Donnez l'heure de début de la location (un entier) : "))
fin = int(input("Donnez l'heure de fin de la location (un entier) : "))

duree_location = fin - debut

cout_total = 0
for heure in range(debut, fin):
    if heure < 7 or (heure >= 17 and heure < 24):
        cout_total += 1
    else:
        cout_total += 2

# Affichage des résultats
print(f"Vous avez loué votre vélo pendant {duree_location} heure(s).")
print(f"Le montant total à payer est de {cout_total:.1f} euro(s).")