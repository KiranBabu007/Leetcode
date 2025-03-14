# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        
        curr=head
        q=deque()
        dummy=head
        ptr=head
        while(curr):
            if curr.val>=x:
                q.append(curr.val)
            else:
                ptr.val=curr.val
                ptr=ptr.next
            curr=curr.next
        for i in q:
            ptr.val=i
            ptr=ptr.next
        return dummy

        