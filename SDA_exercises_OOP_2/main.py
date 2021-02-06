from SDA_exercises_OOP_2.persons import Employee


def employee_test():

    employee_1 = Employee('Jan', 'Kowalski', '1980-01-20', 2300)
    employee_2 = Employee('Adam', 'Mickiewicz', '1798-12-24', 100)

    print(employee_2.manage_salary)
    print(employee_2.who_am_i())


if __name__ == "__main__":
    employee_test()
