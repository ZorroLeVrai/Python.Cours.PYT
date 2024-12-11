annuaire_telephonique = dict()
deco_menu = "="*3

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

def entrer_nom():
    return input("Entrez le nom du contact: ")

def entrer_numero():
    return input("Entrez le numéro du contact: ")

def deco_text(text):
    return f"{deco_menu} {text} {deco_menu}"

def choix_option():
    print(f"""{deco_text("MENU PRINCIPAL")}
1. Voir l'annuaire
2. Ajouter un contact
3. Editer un contact
4. Supprimer un contact
5. Rechercher un numéro de téléphone
0. Quitter le programme""")
    while True:
        choix = input("Votre choix: ")
        try:
            option = int(choix)
            if 0 <= option <= 5:
                return option
            print("Option non disponible. L'option doit être entre >= 0 et <= 5")
        except ValueError:
            print("L'option doit être un entier")

def run():
    while True:
        option = choix_option()

        match option:
            case 0:
                print("Fin du programme")
                break
            case 1:
                print(deco_text("LISTE DES CONTACTS"))
                afficher_contacts()
            case 2:
                print(deco_text("AJOUTER UN CONTACT"))
                nom = entrer_nom()
                numero = entrer_numero()
                ajouter_contact(nom, numero)
            case 3:
                print(deco_text("EDITER UN CONTACT"))
                nom = entrer_nom()
                numero = entrer_numero()
                editer_contact(nom, numero)
            case 4:
                print(deco_text("SUPPRIMER UN NOM DE FAMILLE"))
                nom = entrer_nom()
                supprimer_contact(nom)
            case 5:
                print(deco_text("RECHERCHER UN NUMÉRO DE TÉLÉPHONE"))
                nom = entrer_nom()
                rechercher_numero(nom)
            case _:
                print("Option non valide")


run()