class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ans1=[]
        ans2=[]
        for i in nums1:
            if i not in nums2 and i not in ans1:
                ans1.append(i)
        for i in nums2:
            if i not in nums1 and i not in ans2:
                ans2.append(i)
            
        return [ans1,ans2]

        