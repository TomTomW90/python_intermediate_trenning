from math import log


def power_of_two(n: int) -> bool:
    if log(n, 2) % 2 == 0:
        return True
    else:
        return False


def power_of_two_v2(n: int) -> bool:
    v = 0
    if n in [1, 2]:
        return True
    while 2 ** v <= n:
        if 2 ** v == n:
            return True
        v += 1
    return False


if __name__ == "__main__":
    print(power_of_two_v2(1))
    print(power_of_two_v2(2))
    print(power_of_two_v2(3))
    print(power_of_two_v2(4))
