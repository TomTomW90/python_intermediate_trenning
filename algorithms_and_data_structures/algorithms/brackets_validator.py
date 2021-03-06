def validate_brackets(sequence: str) -> bool:
    left_brackets = []
    right_backets = []
    for bracket in sequence:
        if bracket == '(':
            left_brackets.append(bracket)
        else:
            right_backets.append(bracket)
    if len(left_brackets) == len(right_backets):
        return True
    else:
        return False


if __name__ == '__main__':
    assert validate('((()))') is True
    assert validate('()()()') is True
    assert validate(')))(((') is False  # this might be a problem, check other sollution
    assert validate('((())') is False
