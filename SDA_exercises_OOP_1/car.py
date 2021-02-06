from SDA_exercises_OOP_1.movable import Movable


class Car(Movable):

    def move(self) -> str:
        return f'Jezdze po drogach.'
