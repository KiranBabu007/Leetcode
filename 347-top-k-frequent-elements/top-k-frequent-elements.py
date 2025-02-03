class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c={}
        freq=defaultdict(list)

        c=Counter(nums)
        
        for n,count in c.items():
            freq[count].append(n)
        
        res=[]
        for i in sorted(freq.keys(),reverse=True):
            for nums in freq[i]:
                res.append(nums)
                if len(res)==k:
                    return res
