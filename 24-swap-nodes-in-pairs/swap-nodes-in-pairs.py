# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=head
        curr=head
        while curr and curr.next:
            nxt=curr.next
            nxt.val,curr.val=curr.val,nxt.val
            curr=curr.next.next
        return dummy
        