def factorielle(n, boucle):
    resultat = 1

    if boucle == 'for':
        for i in range(1, n + 1):
            resultat *= i
            print(f"Étape {i}: {resultat}")
    elif boucle == 'while':
        i = 1
        while i <= n:
            resultat *= i
            print(f"Étape {i}: {resultat}")
            i += 1
    else:
        print("Choix invalide. Veuillez choisir 'for' ou 'while'.")

    return resultat

# Demande à l'utilisateur de saisir un entier n
n = int(input("Entrez un entier n pour calculer sa factorielle : "))

# Demande à l'utilisateur de choisir la boucle à utiliser
choix_boucle = input("Choisissez la boucle ('for' ou 'while') : ")

# Calcul de la factorielle en conséquence
result = factorielle(n, choix_boucle)
print(f"La factorielle de {n} est {result}")
