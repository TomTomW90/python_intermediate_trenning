from SDA_exercises_OOP_1.animal import Animal
from SDA_exercises_OOP_1.cat import Cat
from SDA_exercises_OOP_1.dog import Dog


class Vet:

    def say_cat_hello(self, cat: Cat) -> str:
        return f'Hello, little {cat.name}!'

    def say_dog_hello(self, dog: Dog) -> str:
        return f'Hello, brave {dog.name}!'

    def say_hello(self, animal: Animal) -> str:
        return f'Hello, {animal.name}'
