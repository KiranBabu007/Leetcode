class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ans=0
        for i in s:
            ans+=abs(s.find(i)-t.find(i))
        return ans