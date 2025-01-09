class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        p=len(pref)
        c=0
        for w in words:
            
            if w[:p]==pref:
                c+=1
        return c
        