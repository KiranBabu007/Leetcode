class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c={}
        for i in arr:
            if i not in c:
                c[i]=1
            else:
                c[i]+=1
        return len(c.values())==len(set(c.values()))
        