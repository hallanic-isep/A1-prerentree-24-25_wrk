import random


def verifie(cible,essai):
    if cible == essai:
        print("Bravo !!!")
        return True # Résultat "Vrai" si juste prix
    elif cible < essai:
        print("Trop élevé...")
    else:
        print("Trop peu...")
    return False # Résultat "Faux" si différent


# Empêche d'exécuter la suite en cas d' "import" de "juste_prix"
# ... comme dans le cas du lancement d'un test unitaire depuis PyCharm
if __name__ == '__main__':

    cible = random.randint(1,10)
    # Triche...
    #print(f"La cible est {cible}")

    for i in range(5):

        print(f"Essai n°{i+1}...")
        try:
            essai = int(input("Votre proposition entre 1 et 10 : "))
        except ValueError as err:
            print("Valeur incorrecte...")
            print(f"(Message du système : {err})")
            essai = 0 # pour éviter l'erreur si aucune saisie est valide...
            continue


        # Debug : Affiche le type des données
        #print(f"\"cible\" est de type {type(cible)}")
        #print(f'"essai" est de type {type(essai)}')

        # Vérifie si le joueur a trouvé
        if verifie(cible,essai) == True:
            break

    if essai != cible:
        print("Perdu...")

    print("FIN...")
