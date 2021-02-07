def case_1():
    # given
    list_of_numbers = [1, 5, 8, 10, 21]
    # when
    print('Case_1 before')

    # then; wersja pierwsza
    try:
        result = list_of_numbers[5]
    except IndexError as ie:
        print(f'Exception cought by IndexError {ie.args}')
    except Exception as exp:
        print(f'Exception cought by Exception {exp.args}')

    print('Case_1 after')

    # then; wersja druga
    try:
        result = list_of_numbers[5]
    except (IndexError, Exception) as e:
        print(f'Exception cought by touple of (IndexError, Exception) {e.args}')


def case_2(name: str):
    if len(name) == 0:
        raise ValueError('String is empty.')
    print(f"Given name is: {name}")


def case_3(number: int, divisor: int):
    try:
        return number / divisor
    except ZeroDivisionError:
        print(f'Given divisor should not be 0')
        return 0


def case_4(dictionary: dict, key: str):
    try:
        items: list = dictionary[key]
        for item in items:
            print(item)
    except KeyError as ke:
        print(f'Key {ke.args} not found.')


def case_6():
    raise NotImplementedError(f'Solved in the future')


def case_7():
    fd = None
    try:
        fd = open('c:/not_exist/file')
    except IOError as ioe:
        print(f'Eception cought, {ioe.args}')
    finally:
        if fd:
            print('File descriptor closin.')
            fd.close()


def case_7_v2():
    try:
        with open('c:/not_exist/file'):
            print("File is open")
    except IOError as ioe:
        print(f'Exception cought {ioe.args}')