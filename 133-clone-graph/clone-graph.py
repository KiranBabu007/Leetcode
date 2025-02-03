"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        adjList={}
        def clone(node):
            if node in adjList:
                return adjList[node]
            cpy=Node(node.val)
            adjList[node]=cpy
            for i in node.neighbors:
                cpy.neighbors.append(clone(i))
            return cpy
        return clone(node)
        
