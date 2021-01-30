class Movable:

    def move(self):
        pass


class Car(Movable):

    def move(self) -> str:
        return "I am moving"


class Cat(Movable):

    def __init__(self, name: str):
        self._name = name
        self._no_of_eaten_mouses = 0

    def get_name(self) -> str:
        return self._name

    def make_sound(self) -> str:
        return f"{self._name} makes 'Meow'"

    def eat_mouse(self) -> str:
        self._no_of_eaten_mouses += 1
        return f"I ate {self._no_of_eaten_mouses} mouses."

    def move(self):
        return "I am walking."


class Dog:

    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def make_sound(self) -> str:
        return f"{self._name} makes 'WoW'"


class Vet:

    @staticmethod
    def say_cat_hello(cat: Cat) -> str:
        return f"Hello, little {cat.get_name()}"

    @staticmethod
    def say_dog_hello(dog: Dog) -> str:
        return f"Hello, good boy {dog.get_name()}"

    @staticmethod
    def say_hello(animal: (Cat, Dog)) -> str:
        return f"Hello, {animal.get_name()}"


list_of_cats = [Cat('Mruczek'), Cat('Kicia'), Cat('Myszka'), Cat('Werka')]
print([cat.make_sound() for cat in list_of_cats])

list_of_animals = [Cat('Mruczek'), Cat('Kicia'), Cat('Myszka'), Dog('Reksio'), Dog('Ciapek'), Dog('Bethoven')]
print([animal.make_sound() for animal in list_of_animals])

print(Vet.say_hello(Cat("Miauczek")))
