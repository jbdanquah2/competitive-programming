class Node:

    def __init__(self, value):
        self.val = value
        self.next = None

def reverse_linked_list(self, head: Node) -> Node:
    curr = head
    prev = None

    #1,2,3,4,5
    while curr:
        next_node = curr.next
        curr.next = next_node.next
        prev = curr
        curr = next_node

    curr 4 . nex 5
    cur.nxt 5 prv 4
    curr 5
/Users/johndanquah-boateng/Documents/A2SV/python-code/competitive-programming/python/reverse_linkedlist.py

python/minimum-number-of-operations-to-move-all-balls-to-each-box.py



