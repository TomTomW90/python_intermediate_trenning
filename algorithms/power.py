def power(x: int, n: int) -> int:
    total = 1
    if n == 0:
        return 1
    for _ in range(0, n):
        total *= x
    return total

if __name__ == '__main__':
    print(power(2, 0))
    print(power(2, 1))
    print(power(2, 2))
    print(power(2, 3))
    print(power(2, 4))
