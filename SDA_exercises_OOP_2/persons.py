from datetime import date as d


class Person:

    def __init__(self, name: str, surname: str, date_of_birth: d):
        self._name = name
        self._surname = surname
        self._date_of_birth = date_of_birth

    @property
    def manage_name(self) -> str:
        return self._name

    @manage_name.setter
    def manage_name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def manage_surname(self) -> str:
        return self._surname

    @manage_surname.setter
    def manage_surname(self, new_surname: str) -> None:
        self._surname = new_surname

    @property
    def manage_date_of_birth(self) -> d:
        return self._date_of_birth

    @manage_date_of_birth.setter
    def manage_date_of_birth(self, date_of_birth: d) -> None:
        self._date_of_birth = date_of_birth


# class Employee(Person):
#
#     @property
#     def manage_date_of_birth(self) -> d:
#         return self._date_of_birth
#
#     @manage_date_of_birth.setter
#     def manage_date_of_birth(self, date_of_birth: d):