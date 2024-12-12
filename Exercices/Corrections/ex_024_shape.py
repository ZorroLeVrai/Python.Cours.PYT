import math

class Shape:
    def __init__(self):
        self.perimeter = self.get_perimeter()
        self.surface = self.get_surface()

    def afficher_perimetre(self) -> None:
        print(f"Perimeter: {self.perimeter}")

    def afficher_surface(self) -> None:
        print(f"Surface: {self.surface}")

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def get_surface(self) -> float:
        return math.pi * self.radius * self.radius
    
    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def get_perimeter(self) -> float:
        return 2 * (self.length + self.width)
    
    def get_surface(self) -> float:
        return self.length * self.width
    
    def __str__(self) -> str:
        return f"Rectangle(length={self.length}, width={self.width})"


class Container:

    def __init__(self):
        self.shapes: list[Shape] = []

    def display_shapes(self) -> None:
        print("Liste de formes")
        for index, item in enumerate(self.shapes):
            print(f"{index} -> {item}")

    def add_shape(self, shape: Shape) -> None:
        self.shapes.append(shape)

    def remove_shape(self, index: int) -> None:
        del self.shapes[index]

    def perimeter(self) -> float:
        perimetre_total = 0
        for shape in self.shapes:
            perimetre_total += shape.perimeter
        return perimetre_total
    
    def surface(self) -> float:
        surface_total = 0
        for shape in self.shapes:
            surface_total += shape.surface
        return surface_total


if __name__ == "__main__":
    conteneur = Container()
    conteneur.add_shape(Rectangle(10, 10))
    conteneur.add_shape(Rectangle(20,10))
    conteneur.add_shape(Circle(2))

    conteneur.display_shapes()
    print("Perimeter", conteneur.perimeter())
    print("Surface", conteneur.surface())
