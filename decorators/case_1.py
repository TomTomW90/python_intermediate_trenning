def wrap_before_and_after(func):
    def wrapper(*args, **kwargs):
        print('Before')
        result = func(*args, **kwargs)
        print('After')
        return result
    return wrapper


@wrap_before_and_after
def print_hello_world(a, b):
    print("Hello world!")
    print(f'{a, b}')
    return a, b
