from contextlib import contextmanager


@contextmanager
def file_manager(path, mode):
    file = open(path, mode)
    yield file
    file.close()


def write_my_file():
    try:
        with file_manager('./testfiel.txt', 'r') as fd:
            fd.write('testowy plik')
    except IOError:
        print('File doesnt exist.')
