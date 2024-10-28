import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        return n==2**int(math.log(n,2))
        