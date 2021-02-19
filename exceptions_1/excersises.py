def case_1():
    # given
    list_of_numbers = [1, 5, 8, 10, 21]
    # when
    print('Case_1 before')
    # then; wersja pierwsza
    try:
        result = list_of_numbers[5]
    except IndexError as ie:
        print(f'Exception couht {ie.args}')
    except Exception as exp:
        print(f'Exception cought {exp.args}')

    print('Case_1 after')

    # then; wersja druga
    try:
        result = list_of_numbers[5]
    except (IndexError, Exception) as e:
        print(f'Exception cought by touple {e.args}')


def case_2(name: str):
    if len(name) <= 0:
        raise ValueError('String is empty.')
    print(f"Given name is: {name}")
