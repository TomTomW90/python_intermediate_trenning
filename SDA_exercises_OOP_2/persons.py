from abc import ABC, abstractmethod
from datetime import date as d


class Person(ABC):

    def __init__(self, name: str, surname: str, date_of_birth: str):  # str must be ISO format: YYYY-MM-DD
        self._name = name
        self._surname = surname
        self._date_of_birth = d.fromisoformat(date_of_birth)

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

    @abstractmethod
    @property
    def manage_date_of_birth(self) -> d:
        return self._date_of_birth

    @abstractmethod
    @manage_date_of_birth.setter
    def manage_date_of_birth(self, date_of_birth: str) -> None:
        self._date_of_birth = d.fromisoformat(date_of_birth)

    @abstractmethod
    def who_am_i(self) -> str:
        pass


class Employee(Person):

    def __init__(self, name: str, surname: str, date_of_birth: str, salary: float):
        super().__init__(name, surname, date_of_birth)
        self._salary = salary

    @property
    def manage_date_of_birth(self):
        return self._date_of_birth

    @manage_date_of_birth.setter
    def manage_date_of_birth(self, date_of_birth: str) -> None:
        date_of_birth = d.fromisoformat(date_of_birth)
        if d(1900, 1, 1).year < date_of_birth.year <= d.today().year:
            self._date_of_birth = date_of_birth
        else:
            self._date_of_birth = 0

    @property
    def manage_salary(self) -> float:
        return self._salary

    @manage_salary.setter
    def manage_salary(self, new_salary: float) -> None:
        self._salary = new_salary

    def who_am_i(self) -> str:
        return f'Nazywam się {self._name} {self._surname} i zarabiam {self._salary}PLN'


class Manager(Employee):

    @property
    def manage_salary(self) -> float:
        bonus = self._salary * 0.1
        return self._salary + bonus

    @manage_salary.setter
    def manage_salary(self, new_salary: float) -> None:
        self._salary = new_salary

    def who_am_i(self) -> str:
        return f'Nazywam się manager {self._name} {self._surname} i zarabiam {self._salary}PLN'
