class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        i,j=0,0
        if not s or not g:
            return 0
        while(i<len(g) and j<len(s)):
            if g[i]<=s[j]:
                j+=1
                i+=1
            else:
                i+=1
        return j


        