from abc import ABC, abstractmethod
from functools import reduce
import math


class Shape(ABC):
    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def surface(self) -> float:
        pass


class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def surface(self) -> float:
        return math.pi * self.radius * self.radius
    
    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)
    
    def surface(self) -> float:
        return self.length * self.width
    
    def __str__(self) -> str:
        return f"Rectangle(length={self.length}, width={self.width})"


class Square(Rectangle):

    def __init__(self, side: float):
        super().__init__(side, side)

    def __str__(self) -> str:
        return f"Square(side={self.length})"


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
        del self[index]

    def perimeter(self) -> float:
        return reduce(lambda accumulator, current: accumulator + current.perimeter(), self.shapes, 0.0)
    
    def surface(self) -> float:
        return reduce(lambda accumulator, current: accumulator + current.surface(), self.shapes, 0.0)


if __name__ == "__main__":
    conteneur = Container()
    conteneur.add_shape(Square(10))
    conteneur.add_shape(Rectangle(20,10))
    conteneur.add_shape(Circle(2))

    conteneur.display_shapes()
    print("Perimeter", conteneur.perimeter())
    print("Surface", conteneur.surface())
