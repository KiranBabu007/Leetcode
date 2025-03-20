# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        vis=set()

        
        while curr:
            if curr in vis:
                return curr
            vis.add(curr)
            curr=curr.next
        
        

        