class Cat:

    def __init__(self, name: str, saund: str = 'Meow', eaten_mauses: int = 0):
        self.name = name
        self.saund = saund
        self.eaten_mauses = eaten_mauses

    def make_sound(self) -> str:
        return f"{self.name} makes {self.saund}"

    def eat_mouse(self) -> None:
        self.eaten_mauses += 1

    def count_eaten_mouses(self) -> int:
        print(f'{self.name} ate {self.eaten_mauses} mauses.')
        return self.eaten_mauses
