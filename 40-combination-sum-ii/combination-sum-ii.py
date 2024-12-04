class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findComb(ind,arr,t,ans,path):
            if t==0:
                ans.append(list(path))
                return
            for i in range(ind,len(arr)):
                if i>ind and arr[i]==arr[i-1]:
                    continue
                if arr[i]>t:
                    break
                path.append(arr[i])
                findComb(i+1,arr,t-arr[i],ans,path)
                path.pop()
        ans=[]
        candidates.sort()
        findComb(0,candidates,target,ans,[])
        return ans
        