class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not prerequisites:
            return [i for i in range(numCourses)]

        pre={i:[] for i in range(numCourses)}
        for start,end in prerequisites:
            pre[start].append(end)

        visited=set()
        cycle=set()
        ans=[]
        def dfs(node):
            if node in visited:
                return True
            if node in cycle:
                return False
            
            cycle.add(node)

            for n in pre[node]:
                if not dfs(n):
                    return False
            cycle.remove(node)
            visited.add(node)
            ans.append(node)
            return True
 
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans




        