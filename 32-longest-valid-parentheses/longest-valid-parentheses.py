class Solution(object):
    def longestValidParentheses(self, s):
        left,right,ans=0,0,0

        for i in s:
            if i =='(':
                left+=1
            else:
                right+=1
            if(right>left):
                left,right=0,0
            elif(left==right):
                ans=max(ans,left*2)
        left,right=0,0
        for i in s[::-1]:
            if i =='(':
                left+=1
            else:
                right+=1
            if(right<left):
                left,right=0,0
            elif(left==right):
                ans=max(ans,left*2)

        

        return ans


        