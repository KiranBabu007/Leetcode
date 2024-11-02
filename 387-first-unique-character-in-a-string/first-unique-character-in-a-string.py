class Solution(object):
    def firstUniqChar(self, s):
        c={}
        for i in s:
            c[i]=c.get(i,0)+1
        
        for i,key in enumerate(s):
            if c[key]==1:
                return i
        return -1

        