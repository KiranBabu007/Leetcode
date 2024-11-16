class Solution(object):
    def addStrings(self, num1, num2):
        res=[]
        carry=0
        i=len(num1)-1
        j=len(num2)-1

        while i>=0 or j>=0:
            c1=int(num1[i]) if i>=0 else 0
            c2=int(num2[j]) if j>=0 else 0
            csum=c1+c2+carry
            res.append(str(csum%10))
            carry=csum // 10

            i-=1
            j-=1
        if carry:
            res.append(str(carry))
        return ''.join(reversed(res))

        
        