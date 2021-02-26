# from serialization.pickle_trenning import pickle_write, pickle_read
# from serialization.csv_trenning import csv_write, csv_read
from serialization.human import write_json_humans, Human


def main():

    users = [
        ('Jan', 'Kowalski', 8090540605),
        ('Ala', 'Makota', 8400605704),
        ('John', 'Doe', 999999999)
    ]

    """Case_1"""
    # pickle_write(users)

    """Case_2"""
    # print(pickle_read('./data.pickle'))

    """Case_3"""
    # csv_write(users)

    """Case_4"""
    # csv_read('./data.csv')

if __name__ == '__main__':
    main()
