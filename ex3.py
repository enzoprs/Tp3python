import random

x = random.randint(0, 100)
compteur = 0

while True:
    chiffre = int(input("Quelle est la valeur de x ? : "))
    compteur += 1

    if x < chiffre:
        print("Plus petit")
    elif x > chiffre:
        print("Plus grand")
    else:
        print(f"Bien joué ! C'est trouvé en {compteur} essais.")
        break
