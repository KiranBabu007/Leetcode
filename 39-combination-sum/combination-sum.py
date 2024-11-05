class Solution(object):
    def combinationSum(self, candidates, target):   
        def findcomb(i,arr,t,st,ans):

            if t==0:
                ans.append(list(st))
                return

            if i==len(arr):
                return
            
            if arr[i]<=t:
                st.append(arr[i])
                findcomb(i,arr,t - arr[i],st,ans)
                st.pop()
            findcomb(i+1,arr,t,st,ans)

        ans=[]
        findcomb(0,candidates,target,[],ans)

        return ans

            
        