class Solution(object):
    def isBalanced(self, num):
        
        sum1=sum([int(num[i]) for i in range(len(num)) if i%2==0])
        sum2=sum([int(num[i]) for i in range(len(num)) if i%2!=0])

        return sum1==sum2
        