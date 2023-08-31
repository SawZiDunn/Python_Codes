class Node:
    def __init__(self, data: int):
        self.data = data
        self.before = None
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None


def printlist(n):
    while n != None:
        print(n.data)
        n = n.next


if __name__ == "__main__":
    linked_list = Linked_list()
    first = Node(25)
    linked_list.head = first

    second = Node(30)
    third = Node(35)
    fourth = Node(40)

    linked_list.head.next = second
    linked_list.head.before = fourth

    second.next = third
    second.before = linked_list.head

    third.next = fourth
    third.before = second

    fourth.before = third
    fourth.next = linked_list.head

    printlist(linked_list.head)
