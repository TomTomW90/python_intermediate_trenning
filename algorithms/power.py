def power(x: int, n: int) -> int:

    if n == 0:
        return 1
    if n > 0:
        total = 1
        for _ in range(0, n):
            total *= x
        return total
    if n < 0:
        total = 1 / power(x, n*(-1))
        return total

if __name__ == '__main__':
    print(power(3, -2))
    print(power(3, -1))
    print(power(3, 0))
    print(power(3, 1))
    print(power(3, 2))
    print(power(3, 3))
