if __name__ != "__main__":
    exit()


nom_fichier = "mon_fichier.txt"
with open(nom_fichier, 'r') as fichier:
    # Lire tout le contenu du fichier
    contenu = fichier.read()
    # Afficher le contenu
    print(contenu)
# Appel de fichier.close() automatiquement à la fin du bloc with