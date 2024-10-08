# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l=[]
        ptr=head
        while(ptr):
            if ptr.next in l:
                return True

            l.append(ptr.next)
            ptr=ptr.next
        return False



        
        