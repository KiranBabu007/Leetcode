class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        nums.reverse()

        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])

        

        