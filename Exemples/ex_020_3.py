# Dictionnaire pour stocker les numéros de téléphone
contacts = {
    "Alice": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012",
    "David": "456-789-0123",
    "Emma": "567-890-1234"
}

nom_recherche = input("Entrez le nom de la personne dont vous voulez obtenir le numéro de téléphone: ")
# Rechercher le numéro de téléphone dans le dictionnaire
numero = contacts.get(nom_recherche)

# Afficher le résultat
if numero:
    print(f"Le numéro de téléphone de {nom_recherche} est {numero}.")
else:
    print(f"Désolé, le numéro de téléphone de {nom_recherche} n'est pas disponible.")
