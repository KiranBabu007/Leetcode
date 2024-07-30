class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        c=1
        ans=1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:  # Check if consecutive
                c += 1
                ans = max(ans, c)
            elif nums[i] != nums[i - 1]:  # If it's not a duplicate, reset count
                c = 1
        return ans
        