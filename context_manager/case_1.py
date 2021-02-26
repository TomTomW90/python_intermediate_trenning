from contextlib import contextmanager


@contextmanager
def file_manager(file_name, mode):
    file = open(file_name, mode)
    yield file
    file.close()
