class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        q=deque()
        profit=0
        for i in prices: 
            if not q:
                q.append(i)
            elif q[-1]<i:
                q.append(i)
            else:
                if len(q)==1:
                    q.pop()
                else:
                    profit+=(q.pop()-q.popleft())
                    q=deque()
                q.append(i)  
        if len(q)>1:
            profit+=(q.pop()-q.popleft())
        return profit
        

        