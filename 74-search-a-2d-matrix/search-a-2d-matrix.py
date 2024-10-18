class Solution(object):
    def searchMatrix(self, matrix, target):
        for nums in matrix:
            low,high=0,len(nums)-1

            while(low<=high):
                mid=(low+high)//2

                if target==nums[mid]:
                    return True
                if nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
        return False