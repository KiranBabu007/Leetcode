class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        
        while part in s:
            n=s.index(part)
            s=s[:n]+s[n+len(part):]
            
        return s
        