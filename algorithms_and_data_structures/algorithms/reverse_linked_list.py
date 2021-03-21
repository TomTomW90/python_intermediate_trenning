from collections import deque

linked_list = deque()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)


def reverse_linked_list(linkedlist: deque) -> deque:
    returned_list = deque()
    while linkedlist:
        returned_list.append(linkedlist.pop())
    return returned_list

if __name__ == '__main__':
    print(linked_list)
    print(reverse_linked_list(linked_list))
