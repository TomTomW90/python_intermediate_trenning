from functools import wraps


def catch_io_error_with_wraps(func):
    @wraps(func)  # zapamiętuje ścieżkę wywołań!
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as e:
            print(f"IOError cougth it {e.args}")
            return None

    return inner


@catch_io_error_with_wraps
def read_does_not_exist_file():
    with open("./training.training.training", "r") as fd:
        fd.read()
