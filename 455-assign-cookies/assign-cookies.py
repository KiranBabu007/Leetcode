class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        if not s or not g:
            return 0
        l=r=0
        while l<len(g) and r<len(s):
            if g[l]<=s[r]:
                l+=1
            r+=1
        return l
