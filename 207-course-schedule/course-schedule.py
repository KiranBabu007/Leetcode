class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjList={i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            adjList[b].append(a)
        Visited=set()
        def dfs(node):
            if node in Visited:
                return False
            Visited.add(node)
            for i in adjList[node]:
                if(not dfs(i)): return False

            Visited.remove(node)
            adjList[node]=[]
            return True
            


        for i in range(numCourses):
            if not dfs(i): return False
        return True
        