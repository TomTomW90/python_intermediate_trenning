
class OpenFileManager:
    def __init__(self, mode: str = 'a', path: str = ""):
        self.__source = path
        self.__mode = mode
        self.__fd = None

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, path: str):
        self.__source = path

    def __enter__(self):
        print('opening file')
        self.__fd = open(self.__source, self.__mode)
        return self.__fd

    def __exit__(self, *args):
        print('closing file')
        self.__fd.close()


def my_file_manager():
    file_manager = OpenFileManager()
    file_manager.source = "./test_file.txt"
    try:
        with file_manager as fd:
            print("Writing")
            fd.write("Tekst")
    except IOError as e:
        print(f"We have an error: {e.args}")
