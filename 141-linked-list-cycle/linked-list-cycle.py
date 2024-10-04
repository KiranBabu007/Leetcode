# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        f,s=head,head

        while(f.next!=None and f.next.next!=None):
            s=s.next
            f=f.next.next

            if(f==s):
                return True
        return False