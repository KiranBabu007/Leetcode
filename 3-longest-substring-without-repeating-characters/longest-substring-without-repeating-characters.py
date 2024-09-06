class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l,ans=0,0
        charSet=set()

        for r in range(len(s)):
            while(s[r] in charSet):
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            ans=max(ans,len(charSet))
            print(charSet)
        return ans

            

        
        