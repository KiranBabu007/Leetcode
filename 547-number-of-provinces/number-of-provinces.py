class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        p=[i for i in range(n)]
        rank=[1] * n

        def find(node):
            while node != p[node]:
                p[node]=p[p[node]]
                node=p[node]
            return node

        def union(n1,n2):
            p1,p2=find(n1),find(n2)

            if p1==p2:
                return 0
            if rank[p2]>rank[p1]:
                p[p1]=p2
                rank[p2]+=rank[p1]
            else:
                p[p2]=p1
                rank[p1]+=rank[p2]
            return 1

        ans=n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:  
                    ans -= union(i, j)
        return ans
        