class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited=set()
        ans=n
        while(n!=1):
            ans=0
            for i in range(len(str(n))):
                num=n%10
                n=n/10
                ans+=num**2
            if ans in visited:
                return False
            else:
                visited.add(ans)
            n=ans

        return True
        
        
        