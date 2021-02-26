def case_1():

    list_of_numbers = [1, 5, 8, 10, 21]

    try:
        result = list_of_numbers[5]
        return result
    except IndexError as ie:
        print(f'Exception cought by IndexError {ie.args}')
    except Exception as exp:  # bad practice, do not use general exception 'Exception'
        print(f'Exception cought by Exception {exp.args}')


def case_2(name: str):
    if len(name) == 0:
        raise ValueError('String is empty.')
    print(name)


def case_3(number: int, divisor: int):
    try:
        return number / divisor
    except ZeroDivisionError as zde:
        print(f'Given divisor should not be 0 {zde.args}')
        return 0


def case_4(dict_of_lists: dict, list_to_be_printed: str):
    try:
        print(dict_of_lists[list_to_be_printed])
    except KeyError:
        print(f'Key representing list: "{list_to_be_printed}" not found.')


def case_6():
    raise NotImplementedError(f'To be solved in the future')


def case_7():
    fd = None
    try:
        fd = open('c:/not_exist/file')
    except IOError as ioe:
        print(f'Eception cought, {ioe.args}')
    finally:
        if fd:
            print('File descriptor closing.')
            fd.close()


def case_7_v2():
    try:
        with open('c:/not_exist/file'):
            print("File is open")
    except IOError as ioe:
        print(f'Exception cought {ioe.args}')
