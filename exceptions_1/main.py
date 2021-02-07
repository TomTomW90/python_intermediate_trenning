from exceptions_1.excersises import case_1, case_2


def main():
    print('Start up')

    try:
        case_2('')
    except ValueError as ve:
        print(f'{ve.args} returned')

    print('Finish')


if __name__ == '__main__':
    main()
