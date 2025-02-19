class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero=0
        two=len(nums)-1
        p=0
        while p<=two:
            if nums[p]==0:
                nums[p],nums[zero]=nums[zero],nums[p]
                zero+=1
            if nums[p]==2:
                nums[p],nums[two]=nums[two],nums[p]
                two-=1
            else:
                p+=1
            
        
            

        