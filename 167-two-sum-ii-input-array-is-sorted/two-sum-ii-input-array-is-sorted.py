class Solution(object):
    def twoSum(self, numbers, target):
        l,r=0,len(numbers)-1

        while(True):
            if numbers[l]+numbers[r] == target:
                return [l+1,r+1]
            if numbers[l]+numbers[r] > target:
                r-=1
            else:
                l+=1
                
        