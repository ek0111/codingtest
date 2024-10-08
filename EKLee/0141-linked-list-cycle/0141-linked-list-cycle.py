# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head
        while tortoise != None and hare != None:
            tortoise = tortoise.next
            if tortoise == None:
                return False
            hare = hare.next
            if hare == None:
                return False
            hare = hare.next
            if tortoise == hare:
                return True
        return False
        