class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjList=defaultdict(list)

        for start,end in prerequisites:
            adjList[start].append(end)

        visited=set()
        
        def takeCourse(i):
            if i in visited:
                return False
            if not adjList[i]:
                return True
            visited.add(i)
            for neighbours in adjList[i]:
                if not takeCourse(neighbours):
                    return False
            adjList[i]=[]
            visited.remove(i)
            return True
            
            
        for i in range(numCourses):
            if not takeCourse(i):
                return False
        return True

