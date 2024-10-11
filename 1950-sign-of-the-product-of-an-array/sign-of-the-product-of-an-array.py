class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(product):
            if product > 0:
                return 1
            elif product<0:
                return -1
            else:
                return 0
        prd=1
        for i in nums:
            prd*=i
        return signFunc(prd)
        

        