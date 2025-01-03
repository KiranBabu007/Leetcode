class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sc=Counter(s)
        tc=Counter(t)

        return sc==tc
        