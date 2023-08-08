class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printlist(n):
    while n != None:
        print(n.data)
        n = n.next


head = Node(10)
one = Node(20)
two = Node(30)
three = Node(35)

head.next = one
one.next = two
two.next = three

printlist(head)
