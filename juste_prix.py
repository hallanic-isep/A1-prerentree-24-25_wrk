import random
cible = random.randint(1,10)
# Triche...
#print(f"La cible est {cible}")

for i in range(5):

    essai = int(input("Votre proposition entre 1 et 10 : "))

    # Debug : Affiche le type des données
    #print(f"\"cible\" est de type {type(cible)}")
    #print(f'"essai" est de type {type(essai)}')

    if cible == essai:
        print("Bravo !!!")

        # Force la fin de la boucle
        break

    elif cible < essai:
        print("Trop élevé...")
    else:
        print("Trop peu...")

if essai != cible:
    print("Perdu...")

print("FIN...")
