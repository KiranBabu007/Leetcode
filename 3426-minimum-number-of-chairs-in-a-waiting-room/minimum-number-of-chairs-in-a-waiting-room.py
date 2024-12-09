class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        chair=0
        for i in s:
            if ans>0 and i=='L':
                ans-=1
            if i=='E':
                ans+=1
                chair=max(ans,chair)
        return chair
        