from SDA_exercises_OOP_1.animal import Animal


class Dog(Animal):

    def __init__(self, name: str, sound: str = 'WoW'):
        super().__init__(name, sound)

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"
