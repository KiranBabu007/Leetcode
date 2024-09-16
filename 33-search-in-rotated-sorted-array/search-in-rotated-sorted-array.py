class Solution(object):
    def search(self, nums, target):
        l,r=0,len(nums)-1
        
        while(l<=r):
            mid=(l+r)//2
            
            if target==nums[mid]:
                return mid

            if nums[mid]>=nums[l]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
            

        