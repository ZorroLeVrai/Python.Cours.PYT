hauteur = int(input("Saisir la hauteur du triangle: "))
for line_index in range(hauteur):
    nb_stars = line_index * 2 + 1
    nb_spaces = hauteur - line_index - 1
    stars = "*"*nb_stars
    spaces = " "*nb_spaces
    print(f"{spaces}{stars}")