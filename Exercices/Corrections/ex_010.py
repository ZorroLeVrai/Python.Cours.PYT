def moyenne(nombre1: float, nombre2: float) -> float:
    return (nombre1 + nombre2) / 2


if __name__ == "__main__":
    print("Calcul de la moyenne")
    nombre1 = float(input("Entrez le premier nombre: "))
    nombre2 = float(input("Entrez le deuxieme nombre: "))
    resultat = moyenne(nombre1, nombre2)
    print(f"La moyenne est de {resultat}")
