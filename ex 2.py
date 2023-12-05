import time

x = int(input("Merci de saisir un nombre supérieur à 1 : "))

print("Avec for:")
for i in range(x, -1, -1):
    print(i)
    time.sleep(0.2)

print("Avec While:")
while x >= 0:
    print(x)
    x -= 1
    time.sleep(0.2)