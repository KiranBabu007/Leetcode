from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjList = defaultdict(list)

        for start, end in prerequisites:
            adjList[start].append(end)

        visited = set()
        order = []

        def takeCourse(i):
            if i in visited:
                return False
            if not adjList[i]:  # No prerequisites left
                if i not in order:
                    order.append(i)
                return True

            visited.add(i)
            for neighbor in adjList[i]:
                if not takeCourse(neighbor):
                    return False
            adjList[i] = []  
            visited.remove(i)

            if i not in order:
                order.append(i)

            return True

        for i in range(numCourses):
            if not takeCourse(i):
                return []

        return order  
