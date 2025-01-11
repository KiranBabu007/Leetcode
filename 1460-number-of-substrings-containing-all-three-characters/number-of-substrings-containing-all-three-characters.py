class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={'a':-1,'b':-1,'c':-1}
        ans=0
        
        for i in range(len(s)):
            hashmap[s[i]]=i
            if hashmap['a']!=-1 and hashmap['b']!=-1 and hashmap['c'] !=-1:
                ans+=(1+min(hashmap['a'],hashmap['b'],hashmap['c']) )   
        return ans



        