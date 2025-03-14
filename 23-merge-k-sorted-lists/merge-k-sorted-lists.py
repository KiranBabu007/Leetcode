# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        arr=[]
        for l in lists:
            while l:
                arr.append(l.val)
                l=l.next
        arr.sort()
        curr=dummy
        for i in arr:
            l=ListNode(i)
            curr.next=l
            curr=curr.next
        return dummy.next

        