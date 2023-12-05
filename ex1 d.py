x = int(input("Merci de saisir un nombre supérieur à 1 : "))
somme = 0
indice = 0

while somme <= x:
    indice += 1
    somme += indice

print(f"Le nombre N recherché est {indice - 1}")
