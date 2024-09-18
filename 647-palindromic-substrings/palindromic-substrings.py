class Solution(object):
    def countSubstrings(self, s):
        c=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                pali=s[i:j+1]
                if pali==pali[::-1]:
                    c+=1
        return c
        