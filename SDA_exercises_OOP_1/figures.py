from math import pi


class Figure:

    def get_area(self) -> float:
        pass


class Rectangle(Figure):

    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width


class Circle(Figure):

    def __init__(self, radius: float):
        self.radius = radius
        self.pi = pi

    def get_area(self):
        return self.pi * self.radius**2


class Triangle(Figure):

    def __init__(self, height: float, base: float):
        self.height = height
        self.base = base

    def get_area(self) -> float:
        return (self.height * self.base)/2


def count_total_area(*args) -> float:
    total = 0
    for figure in args:
        total += figure.get_area()
    return total


def is_pain_enough(pain_coverage, *args) -> bool:
    figures_area = count_total_area(*args)
    return pain_coverage >= figures_area


print(is_pain_enough(20, Rectangle(2, 3), Rectangle(4, 4)))
print(is_pain_enough(21.99, Rectangle(2, 3), Rectangle(4, 4)))
print(is_pain_enough(22, Rectangle(2, 3), Rectangle(4, 4)))
print(is_pain_enough(30, Rectangle(2, 3), Rectangle(4, 4)))
