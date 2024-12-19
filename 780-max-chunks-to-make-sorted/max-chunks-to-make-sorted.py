class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans=0
        m=0
        for i in range(len(arr)):
            m=max(m,arr[i])
            if(m==i):
                ans+=1
        return ans


        