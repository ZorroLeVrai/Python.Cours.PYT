# Exemple de générateur
def compteur(n):
    """Génère les entiers de 0 à n-1"""
    i = 0
    while i < n:
        yield i
        i += 1


for nombre in compteur(5):
    print(nombre)
