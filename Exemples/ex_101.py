#Récupération des arguments passés en ligne de commandes
import sys

if __name__ != "__main__":
    exit()

if len(sys.argv) < 3:
    raise TypeError("Pas assez d'arguments. Vous devez avoir au moins 2 arguments")

# Récupérer la liste des arguments
mot_a_afficher = sys.argv[1]
nombre_de_fois = int(sys.argv[2])

for _ in range(nombre_de_fois):
    print(mot_a_afficher)
