nb_termes = int(input("Entrez le nombre de termes à afficher: "))

if nb_termes < 0:
    print("Le terme ne peut pas être négatif")
    quit()
elif nb_termes == 0:
    print([0])
    quit()
elif nb_termes == 1:
    print([0,1])
    quit()

liste_fibonacci = [0,1]
for index in range(2, nb_termes+1):
    liste_fibonacci.append(liste_fibonacci[index-1] + liste_fibonacci[index-2])

print(liste_fibonacci)