class Solution(object):
    def checkPerfectNumber(self, num):
        if num<6:
            return False
        s=1
        for i in range(2,int(sqrt(num))+1):
            if num%i==0:
                s+=i+num/i
                print(s)
                
        return s==num
        
        
            