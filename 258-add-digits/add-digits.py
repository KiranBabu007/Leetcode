class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while(len(str(num))>1):
            newnum=0
            for i in str(num):        
                newnum+=int(i)       
            num=newnum
        return num
        