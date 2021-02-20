from serialization.csv_trenning import csv_write
from serialization.human import write_json_humans, Human
from serialization.pickle_trenning import pickle_write, pickle_read


def main():

    # users = [
    #     ('Jan', 'Kowalski', 8090540605),
    #     ('Ala', 'Makota', 8400605704),
    #     ('John', 'Doe', 999999999)
    # ]
    #
    # csv_write(users)

    humans = json_human_from_file()
    for human in humans:
        print(human)


if __name__ == '__main__':
    main()
