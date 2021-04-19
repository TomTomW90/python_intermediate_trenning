from re import search


if __name__ == '__main__':

    s = 'foo12bar3'
    print(search('[0-9][0-9][0-9]', s))
