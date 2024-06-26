class Solution(object):
    def isSubsequence(self, s, t):
        p=0
        for i in s:
            while p < len(t) and i != t[p]:
                p+=1
            if p==len(t):
                return False
            p+=1
        return True
                
        

        