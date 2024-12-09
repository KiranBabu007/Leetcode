class Solution(object):
    def isArraySpecial(self, nums, queries):
        ans=[]
        n=len(nums)
        prefix=[0]*n
        for i in range(1,n):
            prefix[i]=prefix[i-1]
            if (nums[i-1]%2==nums[i]%2):
                prefix[i]+=1
        for left, right in queries:
            special_count = prefix[right] - (prefix[left] if left > 0 else 0)
            ans.append(special_count == 0)
        return ans