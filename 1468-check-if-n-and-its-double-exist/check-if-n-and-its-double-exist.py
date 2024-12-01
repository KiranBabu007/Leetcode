class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        for i in range(n):
            for j in range(n):
                if arr[i]==arr[j]*2 and i!=j:
                    return True
        return False
        