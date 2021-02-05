class Dog:

    def __init__(self, name: str, saund: str = 'WoW'):
        self.name = name
        self.saund = saund

    def make_sound(self) -> str:
        return f"{self.name} makes {self.saund}"
