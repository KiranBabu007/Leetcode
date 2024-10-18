class Solution(object):
    def search(self, nums, target):
        low,high=0,len(nums)-1

        while(low<=high):
            mid=(low+high)//2

            if target==nums[mid]:
                return mid
            if nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1
        