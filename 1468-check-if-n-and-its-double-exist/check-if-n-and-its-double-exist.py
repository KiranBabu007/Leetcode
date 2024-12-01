class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s=set()
        for i in arr:
            if i*2 in s or (i%2==0 and i//2 in s):
                print(s,i)
                return True
            s.add(i)
        return False