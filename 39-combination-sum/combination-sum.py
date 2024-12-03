class Solution(object):
    def combinationSum(self, candidates, target):

        def findComb(i,can,t,st,ans):
            if t==0:
                ans.append(list(st))
                return
            if i==len(can):
                return
            if t-can[i]>=0:              
                st.append(can[i])
                findComb(i,can,t-can[i],st,ans)
                st.pop()
            findComb(i+1,can,t,st,ans)

        ans=[]
        findComb(0,candidates,target,[],ans)

        return ans