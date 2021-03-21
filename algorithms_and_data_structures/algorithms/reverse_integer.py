from math import fabs


def rev_int(x: int) -> int:
    x_list = [y for y in str(int(fabs(x)))]
    y_list = []
    while x_list:
        y_list.append(x_list.pop())
    sollution = int("".join(y_list))
    if x < 0:
        sollution *= -1
    return sollution


if __name__ == '__main__':
    assert rev_int(123) == 321
    print(rev_int(123))
    assert rev_int(-123) == -321
    print(rev_int(-123))
    assert rev_int(120) == 21
    print(rev_int(120))
    assert rev_int(0) == 0
    print(rev_int(0))
