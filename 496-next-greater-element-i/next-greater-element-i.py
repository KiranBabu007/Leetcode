class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nextMap={}
        stack=[]
        for num in nums2:

            while stack and stack[-1]<num:
                smaller=stack.pop()
                nextMap[smaller]=num

            stack.append(num)

        while stack:
            nogreater=stack.pop()
            nextMap[nogreater]=-1
        
        return [nextMap[num] for num in nums1]
        


        