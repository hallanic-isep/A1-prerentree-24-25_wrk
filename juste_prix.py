import random
cible = random.randint(1,10)
# Triche...
print(f"La cible est {cible}")

essai = int(input("Votre proposition entre 1 et 10 : "))

# Debug : Affiche le type des données
#print(f"\"cible\" est de type {type(cible)}")
#print(f'"essai" est de type {type(essai)}')

if cible == essai:
    print("Bravo !!!")
elif cible < essai:
    print("Trop élevé...")
else:
    print("Trop peu...")
