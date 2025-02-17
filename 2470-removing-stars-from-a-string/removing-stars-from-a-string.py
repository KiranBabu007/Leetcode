class Solution(object):
    def removeStars(self, s):
        ans=[]
        for i in s:
            if i=="*":
                ans.pop()
                continue
            ans.append(i)
        return "".join(ans)
            

            
        