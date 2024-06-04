class Node:

    def __init__(self, value) -> None:
        self.val = value
        self.next = None


def linked_list_to_array(head: Node) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

print(b)

print(linked_list_to_array(a))  # [1, 2, 3]
