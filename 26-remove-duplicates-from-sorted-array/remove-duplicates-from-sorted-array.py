class Solution(object):
    def removeDuplicates(self, nums):
        st=sorted(set(nums))
        j = 0
        for x in st:
            nums[j] = x
            j += 1
        return j
