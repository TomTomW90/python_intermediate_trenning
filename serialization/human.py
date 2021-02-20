import json


class Human:
    def __init__(self, age, name, surname):
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Humna: {self.name} {self.surname} {self.age}'

    @classmethod
    def convert_from_dict(cls, params: dict):
        name = params.get("name", "-")
        surname = params.get("surname", "-")
        age = params.get("age", 0)
        return cls(age, name, surname)


def write_json_humans(humans: list):
    humans_serialize = []

    for human in humans:
        human_dict = human.convert_from_dict()
        humans_serialize.append(human_dict)

    try:
        with open("./trenning.json", 'w') as fd:
            json.dump(humans_serialize, fd, indent=2)
    except (IOError, Exception) as exp:
        print(f'Error while writing file. More info: {exp.args}')


def read_json_humans():
    humans_serialize = []

    try:
        with open("./humans_test.json", "r") as fd:
            humans_serialize = json.load(fd)
    except (IOError, Exception) as e:
        print(f'Problem with writing to file, more info: {e.args}')

    humans = []

    for human_dict in humans_serialize:
        human = Human.convert_from_dict(human_dict)
        humans.append(human)

    return humans
