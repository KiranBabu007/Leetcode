class Solution(object):
    def minWindow(self, s, t):

        if not s:
            return ""
        
        tcount=Counter(t)
        window={}
        have=0
        need=len(tcount)
        l=0
        res,resLen=[-1,-1],float('inf')

        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in tcount and window[c]==tcount[c]:
                have+=1
            while have==need:

                if r-l+1 < resLen:
                    resLen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in tcount and window[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        l,r=res

        return s[l:r+1] if resLen<float("inf") else ""







        