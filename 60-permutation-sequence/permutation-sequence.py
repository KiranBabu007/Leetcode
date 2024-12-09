class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fact=1
        nums=[]
        for i in range(1,n):
            nums.append(i)
            fact*=i
        nums.append(n)
        ans=''
        k=k-1
        while(True):
            ans=ans+str(nums[(k//fact)])
            nums.remove(nums[k//fact])
            k=k%fact
            if len(nums)==0:
                break
            fact=fact//len(nums)
            print(fact,"maari",len(nums))
        return ans
        