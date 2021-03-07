class Stack:
    def __init__(self):
        self._stack = []

    def push(self, key: int) -> None:
        self._stack.append(key)

    def pop(self) -> int:
        if not self._stack:
            raise IndexError("Stack is empty.")
        return self._stack.pop()

    def peek(self) -> int:
        if not self._stack:
            raise IndexError("Stack is empty.")
        return self._stack[-1]


def check_brackets(brackets):  # zamiast sprawdzenia przy pop() zrób przy push
    brackets_stack = Stack()
    for obj in brackets:
        brackets_stack.push(obj)
    last = brackets_stack.pop()
    current = brackets_stack.peek()
    try:
        while last != current:
            last = brackets_stack.pop()
            current = brackets_stack.peek()
    except IndexError:
        return "There is a match."
    return "Dont match"


if __name__ == "__main__":

    b = ['(', ')', '(', ')', '(', ')']

    print(check_brackets(b))
