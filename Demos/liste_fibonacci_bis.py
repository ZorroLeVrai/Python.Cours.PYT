nb_termes = int(input("Entrez le nombre de termes à afficher: "))

if nb_termes < 0:
    print("Le terme ne peut pas être négatif")
    quit()

liste_fibonacci = []
for index in range(0, nb_termes+1):
    match index:
        case 0: liste_fibonacci.append(0)
        case 1: liste_fibonacci.append(1)
        case _: liste_fibonacci.append(liste_fibonacci[index-1] + liste_fibonacci[index-2])

print(liste_fibonacci)