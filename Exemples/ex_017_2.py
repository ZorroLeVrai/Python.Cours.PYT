# Créez une liste contenant des marques de voitures
liste_voiture = []
liste_non_terminee = True
while liste_non_terminee:
    marque_voiture = input("Entrez la marque de la voiture: ")

    if marque_voiture:  #if marque_voiture != "":
        liste_voiture.append(marque_voiture)
    else:
        liste_non_terminee = False

print(liste_voiture)