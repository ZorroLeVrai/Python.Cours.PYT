def afficher_message(message, nb_etoiles):
    print("*"*nb_etoiles, end="") # Affiche des étoiles
    print(f" {message} ", end="") # Affiche un message
    print("*"*nb_etoiles, end="") # Affiche des étoiles
    print() # Retourner à la ligne


afficher_message("Bonjour", 10)
print("Action 1")
afficher_message("Hello", 8)
print("Action 2")
afficher_message("Hallo", 6)
