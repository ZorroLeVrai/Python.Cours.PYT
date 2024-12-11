annuaire_telephonique = dict()

def afficher_contacts():
    for nom, numero in annuaire_telephonique.items():
        print(f"{nom}: {numero}")

def ajouter_contact(nom: str, numero_str: str):
    if nom in annuaire_telephonique:
        print(f"Le contact {nom} est déjà présent dans l'annuaire")
        return

    if numero_str == "":
        print("Le numéro de téléphone doit être renseigné")
        return
    
    annuaire_telephonique[nom] = numero_str
    print(f"Le contact a été enregistré {nom}: {numero_str}")

def editer_contact(nom: str, numero_str: str):
    if nom not in annuaire_telephonique:
        print(f"Le contact {nom} n'est pas présent dans l'annuaire")
        return
    if numero_str == "":
        print("Le numéro de téléphone doit être renseigné")
        return
    
    annuaire_telephonique[nom] = numero_str
    print(f"Le contact a été mis à jour {nom}: {numero_str}")

def supprimer_contact(nom: str):
    if nom not in annuaire_telephonique:
        print(f"Le contact {nom} n'est pas présent dans l'annuaire")
        return
    
    del annuaire_telephonique[nom]
    print(f"Le contact {nom} a été supprimé")

def rechercher_numero(nom: str):
    if nom not in annuaire_telephonique:
        print(f"Le contact {nom} n'est pas présent dans l'annuaire")
        return
    
    print(f"Le numéro est: {annuaire_telephonique[nom]}")


# Test
ajouter_contact("Jean", "0123456789")
ajouter_contact("Jane", "9876543210")
ajouter_contact("John", "11111")

editer_contact("Jane", "55555")

print("Affichage des contacts:")
afficher_contacts()