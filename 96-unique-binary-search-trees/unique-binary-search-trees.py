class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        numTrees=[0] * (n+1)
        numTrees[0]=numTrees[1]=1
        for nodes in range(2,n+1):
            total=0
            for root in range(1,nodes+1):
                l=root-1
                r=nodes-root
                total+=numTrees[l]*numTrees[r]
            numTrees[nodes]=total
        return numTrees[n]
        