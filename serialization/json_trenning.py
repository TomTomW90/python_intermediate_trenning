import json


def write_json():
    json_list = [
        {'name': 'Ala'},
        {'name': 'John'},
    ]

    try:
        with open("./trenning.json", 'w') as fd:
            json.dump(json_list, fd, indent=2)
    except (IOError, Exception) as exp:
        print(f'Error while writing file. More info: {exp.args}')


def read_json():
    json_list = []

    try:
        with open("./training.json", "r") as fd:
            json_list = json.load(fd)

    except (IOError, Exception) as exp:
        print(f'Problem with writing to file, more info: {exp.args}')

    return json_list
