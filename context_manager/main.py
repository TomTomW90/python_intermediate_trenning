# from context_manager.case_1 import file_manager
from context_manager.case_2_3 import my_file_manager


def main():

    """case_1"""
# try:
#     with file_manager('testfile.txt', 'w') as fd:
#         fd.write('')
# except IOError:
#     print('File doesnt exist.')

    """case_2"""
    my_file_manager()


if __name__ == '__main__':
    main()
