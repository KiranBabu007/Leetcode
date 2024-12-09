class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        c=Counter(stones)
        ans=0
        for i in jewels:
            if i in c:
                ans+=c[i]
        return ans

        