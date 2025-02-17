class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1=[]
        for i in s:
            if i=="#":
                if l1:
                    l1.pop()
                continue
            l1.append(i)
        l2=[]
        for i in t:
            if i=="#":
                if l2:
                    l2.pop()
                continue
            l2.append(i)
        
        return l1==l2
        
        