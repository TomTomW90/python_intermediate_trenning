from serialization.csv_trenning import csv_write
from serialization.pickle_trenning import pickle_write, pickle_read


def main():

    users = [
        ('Jan', 'Kowalski', 8090540605),
        ('Ala', 'Makota', 8400605704),
        ('John', 'Doe', 999999999)
    ]

    csv_write(users)


if __name__ == '__main__':
    main()
