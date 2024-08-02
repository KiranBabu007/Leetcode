class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=''
        l=list(zip(*strs))

        for i in l:
            if len(set(i))==1:
                ans+=i[0]
            else:
                break
        return ans


        