from os.path import exists

nom_fichier = "secret.txt"

def lire_secret():
    if not exists(nom_fichier):
        return ""
    
    with open(nom_fichier, "r") as fichier:
        return fichier.read()


def ecriture_secret(secret):
    with open(nom_fichier, "w") as fichier:
        fichier.write(secret)


if __name__ == "__main__":
    secret = lire_secret()

    while True:
        option = input("""Choisir une action
            1: Voir le secret
            2: Modifier le secret
            3: Quitter le programme
            """)

        match option:
            case "1":
                if secret:
                    print(f"Le secret est {secret}")
                else:
                    print(f"Il n'y a pas de secret")
            case "2":
                secret = input("Saisir le secret: ")
            case "3":
                ecriture_secret(secret)
                print ("Au revoir")
                break

    print("Fin du programme")
