# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        curr=head
        Dummy=ListNode(next=head)
        prev=Dummy
        
        while(curr):
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
                     
        return Dummy.next

        