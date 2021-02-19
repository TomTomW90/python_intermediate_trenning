from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):

    @abstractmethod
    def get_area(self) -> float:
        pass

    @staticmethod
    def add_areas(*args) -> float:
        total_area = 0
        for figure in args:
            total_area += figure.get_area()
        return total_area

    @staticmethod
    def check_if_there_is_enough_paint(area_tobe_painted, *args) -> bool:
        return area_tobe_painted <= Figure.add_areas(*args)


class Rectangle(Figure):

    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def get_area(self) -> float:
        return self.height * self.width


class Circle(Figure):

    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return pi * self.radius**2


class Triangle(Figure):

    def __init__(self, basis: float, height: float):
        self.basis = basis
        self.height = height

    def get_area(self) -> float:
        return (self.height * self.basis)/2
