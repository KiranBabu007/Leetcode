class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen=set()
        ans=set()

        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                ans.add(s[i:i+10])
            seen.add(s[i:i+10])
        return list(ans)

        