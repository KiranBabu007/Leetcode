class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=""
        for i in s:
            if i=="#":
                s1=s1[:-1]
                continue
            s1+=i
        s2=""
        for i in t:
            if i=="#":
                s2=s2[:-1]
                continue
            s2+=i
        
        return s1==s2
        
        