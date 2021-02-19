from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    @abstractmethod
    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"
