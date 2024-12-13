import os
import glob

#Liste tous les fichiers se terminant par .txt
liste_fichiers = glob.glob("*.txt")
print("Liste des fichiers .txt:", liste_fichiers)

print(os.path.join(r"C:\Users\orsys", "test.txt"))
# Output: C:\Users\orsys\test.txt

repertoire, fichier = os.path.split(r"C:\Users\orsys\test.txt")
print(f"Répertoire: {repertoire}, Fichier: {fichier}")

print(os.path.exists(r"C:\Users\orsys\test.txt"))
# Output: False

# Création d'un répertoire
if not os.path.exists("mon_repertoire"):
    os.makedirs("mon_repertoire")

# Renommer un fichier
if os.path.exists("test4.py"):
    os.rename("test4.py", "test9.py")

# Déplacer un fichier
if os.path.exists("test9.py"):
    os.rename("test9.py", r"tests\test9.py")


