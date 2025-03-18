class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        adjList=defaultdict(list)
        for start,end,price in flights:
            adjList[start].append([end,price])
        

        heap=[[0,src,0]]
        minprice=float('inf')
        visited=set()
        while heap:
            p,n,i=heappop(heap)
            if (n,i) in visited:
                continue
            visited.add((n,i))
            if i>k:
                continue
            for dest,price in adjList[n]:
                heappush(heap,[price+p,dest,i+1])
                if dest==dst:
                    minprice=min(minprice,p+price)
        return -1 if minprice==float('inf') else minprice
        

        