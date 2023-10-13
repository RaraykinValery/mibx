from abc import ABC, abstractmethod
import math


class FigureType(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Figure:
    def __init__(self, figure_type: FigureType | None = None):
        self.figure_type = figure_type

    def set_figure_type(self, figure_type: FigureType) -> None:
        self.figure_type = figure_type

    def __getattr__(self, name):
        if self.figure_type and hasattr(self.figure_type, name):
            return getattr(self.figure_type, name)
        else:
            raise AttributeError(f"'Figure' object has no attribute '{name}'")


class Circle(FigureType):
    def __init__(self, radius: int | float):
        if radius <= 0:
            raise ValueError("The radius value must be a positive number.")
        self.radius: int | float = radius

    def calculate_area(self) -> float:
        return math.pi * (self.radius**2)


class Triangle(FigureType):
    def __init__(self, a: int | float, b: int | float, c: int | float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError(
                "Values of the lengths of the triangle sides a, b and c "
                "must be positive numbers."
            )
        self.a: int | float = a
        self.b: int | float = b
        self.c: int | float = c

    def calculate_area(self) -> float:
        p: float = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right(self) -> bool:
        sides = [self.a, self.b, self.c]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


if __name__ == "__main__":
    circle = Circle(4)
    print(f"Circle area: {circle.calculate_area()}")

    triangle = Triangle(5, 4, 3)
    print(f"Triangle area: {triangle.calculate_area()}")
    print(f"Is triangle right: {triangle.is_right()}")

    figure = Figure()
    figure.set_figure_type(Circle(4))
    print(f"Figure type circle area: {figure.calculate_area()}")
    figure.set_figure_type(Triangle(5, 4, 3))
    print(f"Figure type triangle area: {figure.calculate_area()}")
    print(f"Figure type triangle is a right triangle: {figure.is_right()}")
