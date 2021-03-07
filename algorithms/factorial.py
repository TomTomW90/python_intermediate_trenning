
def factorial_iter(n: int) -> int:
    if n in [0, 1]:
        return n
    p = 1
    for i in range(2, n+1):
        p *= i
    return p


def factorial_recurency(n: int) -> int:
    if n in [0, 1]:
        return 1
    return n * factorial_recurency(n - 1)


if __name__ == "__main__":
    print(factorial_iter(5))
    print(factorial_recurency(5))
