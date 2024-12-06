class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def findPermu(ind,nums,mapset,path):
            if len(path)==len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if not mapset[i]:
                    mapset[i]=1
                    path.append(nums[i])
                    findPermu(i,nums,mapset,path[:])
                    path.pop()
                    mapset[i]=0
                    
        ans=[]
        mapset=[0 for i in range(len(nums))]
        findPermu(0,nums,mapset,[])
        return ans
        