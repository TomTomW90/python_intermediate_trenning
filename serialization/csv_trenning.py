import csv


def csv_write(list_of_str: list):
    print('csv_write starts')

    try:
        with open('./data.csv', 'a') as fd:
            writer = csv.writer(fd)
            # writer.writerows(list_of_str)
            for row in list_of_str:
                writer.writerow(row)

    except (IOError, Exception) as e:
        print(f'Exception while csv writing {e.args}')

    print('csv_write finish')


def csv_read(csv_file):
    output_list = []
    print('csv_read starts')

    try:
        with open(csv_file) as fd:
            reader = csv.reader(fd)
            for row in reader:
                if row:
                    output_list.append(row)

    except (IOError, Exception) as e:
        print(f'Exception while csv writing {e.args}')

    return output_list

    print('csv_write finish')