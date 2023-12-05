a = 0
b = 0
c = 0

for i in range(10):
    n = float(input("Saisir une valeur entre 0 et 20 : "))

    while n > 20 or n < 0:
        n = float(input("La valeur doit être entre 0 et 20. Réessayez : "))

    if n < 10:
        a += 1
    elif 10 <= n < 15:
        b += 1
    else:
        c += 1

print(f"Nombre de valeurs < 10 : {a}")
print(f"Nombre de valeurs entre 10 et 15 : {b}")
print(f"Nombre de valeurs >= 15 : {c}")
