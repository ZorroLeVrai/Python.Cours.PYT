import os.path
import csv

nom_fichier = "produit.csv"
delimiteur_csv = ";"
nom_titre = "Nom du produit"
prix_titre = "Prix"
stock_titre = "Quantité du stock"


def ajouter_produit(nom: str, prix: float, stock: int):
    """Commentaire Python"""
    fichier_existe = os.path.exists(nom_fichier)

    with open(nom_fichier, "at", newline="", encoding="latin1") as fichier:
        csv_writer = csv.writer(fichier, delimiter=delimiteur_csv)
        if not fichier_existe:
            csv_writer.writerow([nom_titre, prix_titre, stock_titre])
        csv_writer.writerow([nom, prix, stock])

nom = input("Entrez le nom du produit: ")
prix = float(input("Entrez le prix du produit: "))
stock = int(input("Entrer le nombre de produits: "))

ajouter_produit(nom, prix, stock)
