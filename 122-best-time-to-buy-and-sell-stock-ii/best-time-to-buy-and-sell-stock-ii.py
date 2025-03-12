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
                print(q)
                continue
            if q[-1]<i:
                q.append(i)
            else:
                if len(q)==1:
                    q.pop()
                    q.append(i)
                    print(q)
                    continue
                print("empty akanam")
                profit+=(q.pop()-q.popleft())
                while q:
                    q.pop()
                q.append(i)
            print(q)
        if len(q)>1:
            profit+=(q.pop()-q.popleft())
        return profit
        

        