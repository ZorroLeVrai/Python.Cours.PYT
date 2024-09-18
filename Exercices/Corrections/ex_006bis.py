hauteur = int(input("Saisir la hauteur du triangle: "))
nb_padding = 2*hauteur + 1
for line_index in range(0, hauteur):
    nb_stars = 2*line_index+1
    str = "*"*nb_stars
    print(str.center(nb_padding))
    #print(f"{str:^{nb_padding}}")