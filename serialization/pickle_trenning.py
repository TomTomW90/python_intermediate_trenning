import pickle


def pickle_write(items: list):
    print('Pickle_write starts')

    try:
        with open('./data.pickle', 'wb') as fd:
            pickle.dump(items, fd)
            print(pickle.dumps(items))

    except (IOError, Exception) as e:
        print(f'Exception while pickle writing {e.args}')

    print('Pickle_write finish')


def pickle_read(file):

    print('Pickle_read starts')
    string_list = []

    try:
        with open(file, 'rb') as fd:
            string_list = pickle.load(fd)

    except (IOError, Exception) as e:
        print(f'Exception while pickle reading {e.args}')

    print('Pickle_read finish')

    return string_list
