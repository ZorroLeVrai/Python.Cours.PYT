hauteur = int(input("Saisir la hauteur du triangle: "))
nb_padding = 2*hauteur + 1
for i in range(0, hauteur):
    str = "*"*(2*i+1)
    print(str.center(nb_padding))
    #print(f"{str:^{nb_padding}}")