numero = float(input("Entrez le numéro: "))
match numero:
    case 1:
        print("Un")
    case 2:
        print("Deux")
    case _:
        print("Supérieur à deux")
