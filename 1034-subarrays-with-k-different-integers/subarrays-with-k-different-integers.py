class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def calc(g):
            l=0
            res=0
            hashmap={}
            for i in range(len(nums)):
                if g<0:
                    break
                if nums[i] in hashmap:
                    hashmap[nums[i]]+=1
                else:
                    hashmap[nums[i]]=1
                while(len(hashmap)>g):
                    hashmap[nums[l]]-=1
                    if hashmap[nums[l]]==0:
                        hashmap.pop(nums[l])
                    l+=1   
                res+=i-l+1
            return res

        return calc(k)-calc(k-1)
            
            

