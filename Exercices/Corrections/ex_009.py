hauteur_cible_m = 15
hauteur_actuelle_m = 0
ascension_jour_m = 3
glissement_nuit_m = 2
en_journee = True

nb_jours = 0
nb_nuits = 0
while hauteur_actuelle_m < hauteur_cible_m:
    if en_journee:
        hauteur_actuelle_m += ascension_jour_m
        nb_jours += 1
    else:
        hauteur_actuelle_m -= glissement_nuit_m
        nb_nuits += 1

    en_journee = not en_journee

print(f"Durée nécessaire pour l'ascension: {nb_jours} jour(s) et {nb_nuits} nuit(s)")
