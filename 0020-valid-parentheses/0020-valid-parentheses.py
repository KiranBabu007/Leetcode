class Solution(object):
    def isValid(self, s):
        stack=[]
        p={'{':'}','(':')','[':']'}
        for i in s:
            if i in p:
                stack.append(i)
            elif i in p.values():
                if not stack or p[stack.pop()]!=i:
                    return False
        return not stack
           
        
        