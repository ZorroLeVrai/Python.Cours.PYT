import os

repertoire_chemin = r"D:\Users\amine\Documents\GitHub\Python.Cours.PYT\Exemples"

liste_fichier_repertoire = os.listdir(repertoire_chemin)
print("Liste des fichiers dans le répertoire:")

liste_filtree = list(filter(lambda x: x.endswith(".py"), liste_fichier_repertoire))
for element in liste_filtree:
    print(element)
