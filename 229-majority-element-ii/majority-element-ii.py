class Solution(object):
    def majorityElement(self, nums):
        count={}
        l=[]
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1

        m=len(nums)/3
        for i,key in count.items():
            print(m,i,key)
            if key>m:
                l.append(i)
        return l

        


        