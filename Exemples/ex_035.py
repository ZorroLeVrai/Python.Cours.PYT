from abc import ABC, abstractmethod
import math


class Forme(ABC):
    @abstractmethod
    def calculerSurface(self):
        """Calcule et retourne l'aire de la forme"""
        pass

    @abstractmethod
    def calculerPerimetre(self):
        """Calcule et retourne le périmètre de la forme"""
        pass

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculerSurface(self):
        return self.longueur * self.largeur

    def calculerPerimetre(self):
        return 2 * (self.longueur + self.largeur)


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculerSurface(self):
        return math.pi * (self.rayon ** 2)

    def calculerPerimetre(self):
        return 2 * math.pi * self.rayon


sommeSurfaces = 0
formes = [Rectangle(5, 10), Cercle(7)]
for forme in formes:
    sommeSurfaces += forme.calculerSurface()

print("La somme des surfaces", sommeSurfaces)
