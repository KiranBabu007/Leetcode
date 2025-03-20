class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ph = {
    '2': 'abc', '3': 'def',
    '4': 'ghi', '5': 'jkl', '6': 'mno',
    '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}
        ans=[]
        def comb(i,w):
            if i==len(digits):
                ans.append("".join(w))
                return 
            for s in ph[digits[i]]:
                w.append(s)
                comb(i+1,w)
                w.pop()

        comb(0,[])
        return ans
    

        