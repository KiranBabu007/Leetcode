class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c={}

        for i,val in enumerate(s):
            if val not in c:
                if t[i] in c.values():
                    return False
                c[val]=t[i]
            else:
                if c[val]!=t[i]:
                    return False
        return True
            
        