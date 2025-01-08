class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={}
        n=len(s)
        l=0
        r=0
        maxlen=0

        while r<n:
            if s[r] in hashmap:
                if hashmap[s[r]]>=l:
                    l=hashmap[s[r]]+1
            hashmap[s[r]]=r
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen

        