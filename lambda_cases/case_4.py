from random import randrange as r


def digits_manager():
    list_numbers = [r(0, 101) for num in range(10)]
    print(f'Random numbers: {list_numbers}')
    multiplied_list_numbers = list(map(lambda number: number*2, list_numbers))
    print(f'Random numbers: {multiplied_list_numbers}')
    for i in range(10):
        print(f'{list_numbers[i]} : {multiplied_list_numbers[i]}')


def list_sorter():
    list_of_numbers = [r(100, 201) for num in range(20)]
    print(f'Random numbers: {list_of_numbers}')
    list_of_numbers.sort()
    print(f'Random numbers sorted ascending: {list_of_numbers}')
    list_of_numbers.sort(reverse=True)
    print(f'Random numbers sorted descending: {list_of_numbers}')
