class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj=defaultdict(list)
        for u,v,w in times:
            adj[u].append([v,w])

        minheap=[[0,k]]
        shortest={}
        while minheap:
            w1,n1=heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1]=w1
            for n2,w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap,[w1+w2,n2])
        if len(shortest) < n:  
            return -1
        return max(shortest.values())



        