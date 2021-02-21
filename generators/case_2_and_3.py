def number_creator(n):
    list_of_numbers = [number for number in range(n)]
    return list_of_numbers


def iterator_case_2(n):
    import sys
    result_list = number_creator(n)
    result = sum(result_list)
    print(f'Result: {result}')


class Iterable:
    def __init__(self, n):
        self.n = n
        self.generated_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_number >= self.n:
            raise StopIteration
        else:
            self.generated_number += 1
            return self.generated_number


def iterator_case_3(n):
    print("Case_3")
    import sys
    iterator_instance = Iterable(n)
    print(f'Size of iterator_instance in bytes: {sys.getsizeof(iterator_instance)}')
    result = sum(iterator_instance)
    print(f'Size of one number in bytes: {sys.getsizeof(result)}')
    print(f'Result: {result}')
