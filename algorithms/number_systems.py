def as_bin(n: int) -> str:
    if n in [0, 1]:
        return f'0b{str(n)}'
    result = []
    while n != 0:
        n, reminder = divmod(n, 2)
        result.append(str(reminder))
    return f'0b{"".join(result[::-1])}'


def as_ternary(n: int) -> str:
    if n in [0, 1, 2]:
        return f'0t{str(n)}'
    result = []
    while n != 0:
        n, reminder = divmod(n, 3)
        result.append(str(reminder))
    return f'0t{"".join(result[::-1])}'


def as_hex(n: int) -> str:
    hex_dict = {i: str(i) for i in range(10)}
    hex_dict.update({
        10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"
    })
    if n in hex_dict:
        return f'0x{hex_dict[n]}'
    result = []
    while n != 0:
        n, reminder = divmod(n, 16)
        result.append(str(reminder))
    return f'0x{"".join(result[::-1])}'
