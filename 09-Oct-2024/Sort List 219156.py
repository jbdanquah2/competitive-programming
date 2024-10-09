# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or contains only one element
        if not head or not head.next:
            return head
        
        # Helper function to find the middle of the linked list
        def getMiddle(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Split the list into two halves
        middle = getMiddle(head)
        right = middle.next
        middle.next = None  # Disconnect the first half from the second half

        # Recursively sort each half
        left = self.sortList(head)
        right = self.sortList(right)

        # Merge the two sorted halves
        return merge(left, right)

# Helper function to merge two sorted linked lists
def merge(l1, l2):
    dummy = ListNode()  # Dummy node to help with the merge process
    tail = dummy

    # Merge the two lists
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # If any elements are left in either l1 or l2, append them
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

        