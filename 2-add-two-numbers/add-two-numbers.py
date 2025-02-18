# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1=l1
        curr2=l2
        dummy=ListNode()
        curr=dummy
        carry=0

        while curr1 or curr2:
            s=carry
            if curr1:
                s+=curr1.val
            if curr2:
                s+=curr2.val
            l=ListNode(s%10)
            carry=s//10

            curr.next=l
            curr=curr.next

            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next

        if carry>0:
            l=ListNode(carry)
            curr.next=l

        return dummy.next


            

        