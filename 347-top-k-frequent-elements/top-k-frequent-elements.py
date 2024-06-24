class Solution(object):
    def topKFrequent(self, nums, k):
        hash={}
        for i in nums:
            if i not in hash:
             hash[i]=1
            else:
             hash[i]+=1

        sorted_list=sorted(hash.items(),key=lambda x : x[1] ,reverse=True)

        top_k=[item[0] for item in sorted_list[:k]]

        return top_k

        
        