try:
    # Demander à l'utilisateur d'entrer un nombre
    nombre = int(input("Entrez un nombre : "))
    # Effectuer une division par ce nombre
    resultat = 10 / nombre
    print(f"10 divisé par {nombre} donne {resultat}")

# Gestion des erreurs spécifiques
except ValueError:
    print("Erreur : Vous devez entrer un nombre entier.")
except ZeroDivisionError:
    print("Erreur : La division par zéro est impossible.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")
finally:
    print("Fin du programme.")