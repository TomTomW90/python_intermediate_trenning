def number_creator(n):
    list_of_numbers = [number for number in range(n)]
    return list_of_numbers


def iterator_case_2(n):
    print("Case_2")
    import sys
    result_list = number_creator(n)
    print(f'Size of list in bytes: {sys.getsizeof(result_list)}')
    result = sum(result_list)
    print(f'Size of one number in bytes: {sys.getsizeof(result)}')
    print(f'Result: {result}')


class Iterable:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_numbers >= self.n -1:
            raise StopIteration
        self.generated_numbers += 1
        return self.generated_numbers


def iterator_case_3(n):
    print("Case_2")
    import sys
    iterator_instance = Iterable(n)
    print(f'Size of iterator_instance in bytes: {sys.getsizeof(iterator_instance)}')
    result = sum(iterator_instance)
    print(f'Size of one number in bytes: {sys.getsizeof(result)}')
    print(f'Result: {result}')
