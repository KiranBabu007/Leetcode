class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        n=len(nums)
        while(n>1):
            newNums = []
            for i in range(n//2):
                if i%2==0:
                    newNums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    newNums.append(max(nums[2 * i], nums[2 * i + 1]))
            nums=newNums
            n=len(nums)
        return nums[0]
        