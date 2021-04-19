import re


def case_1():
    """Wyciągnij, korzystając z wyrażeń regularnych, z zadanego tekstu, wszystkie liczby."""

    s = 'test43543lfdsfdsfl534543fdgl432fr'
    return re.findall('[0-9]+', s)


def case_1v2():
    """Weź ten sam tekst, co w zadaniu wyżej i napisz program, używając wyrażeń regularnych,
    który usunie wszystkie cyfry z tekstu."""

    s = 'test43543lfdsfdsfl534543fdgl432fr'
    return "".join(re.findall(r'\D+', s))


def case_3(phone_no):
    """Napisz program, który używając wyrażeń regularnych, sprawdzi czy podany numer telefonu jest poprawny."""

    if re.match(r"(\+|00)?48\d{9}", phone_no):
        return phone_no
    else:
        return f'Incorrect phone number'

if __name__ == '__main__':

    print(f'Case 1: {case_1()}')
    print(f'Case 1v2: {case_1v2()}')
    print(f'Case 3: {case_3("+48123456789")}')
