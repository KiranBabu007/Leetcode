class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1=len(a)-1
        l2=len(b)-1

        carry=0
        res=[]

        while l1>=0 or l2>=0:
            b1=int(a[l1]) if l1>=0 else 0
            b2=int(b[l2]) if l2>=0 else 0

            bsum=b1+b2+carry 

            res.append(str(bsum%2))

            carry = bsum//2

            l1-=1
            l2-=1

        if carry>0:
            res.append(str(1))
        
        return ''.join(res[::-1])

