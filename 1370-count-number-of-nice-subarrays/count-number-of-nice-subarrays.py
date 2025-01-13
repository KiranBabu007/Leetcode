class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=[1 if i%2 else 0 for i in nums ]

        def calc(g):
            l=0
            res=0
            s=0
            for i in range(len(nums)):
                if g<0:
                    break
                s+=nums[i]
                while(s>g):
                    s-=nums[l]
                    l+=1   
                res+=i-l+1
            return res
        return calc(k)-calc(k-1)
        