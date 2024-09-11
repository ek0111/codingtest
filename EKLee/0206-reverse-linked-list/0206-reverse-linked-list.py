# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # previous and current = None and head (it is like the dummy node in Swap Nodes in Pair)
        prev = None
        curr = head
        
        #while current is not null (till it reaches the end of the list)
        while curr:
            # next pointer pointing the next node so that we have the pointer to next node
            # even though we may turn the current node pointer to the previous one
            nex = curr.next
            # this is when we turn our curr node pointer to the previous one
            curr.next = prev
            # since we turned our current node pointer to previous, time to update to new previous node
            prev = curr
            # now new current node
            curr = nex
        
        return prev