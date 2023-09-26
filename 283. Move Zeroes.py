# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array


class Solution(object):
    def moveZeroes(self, nums):
        low=0
        for i,num in enumerate(nums):
            if num!=0:
                nums[low],nums[i]=num,nums[low]
                low+=1
