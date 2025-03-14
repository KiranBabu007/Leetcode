class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l=0
        r=len(people)-1
        boat=0
        while(l<=r):
            balance=limit-people[r]
            r-=1
            boat+=1
            if l<=r and people[l]<=balance:
                l+=1
        return boat
        



        

        