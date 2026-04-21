from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# (1)-(2)
#     /
#   (3) 

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        # Declare dict where every key->node, val-> copy_node
        clones = dict()
        clones[node] = Node(node.val)
        # Queue to make sure we visit ever node
        q = deque()
        q.append(node)
        # Iterate while the queue is not empty
        while(q):
            curr = q.popleft()            
            # Add neighbors to clone
            for n in curr.neighbors:
                if n not in clones:
                    clones[n] = Node(n.val)
                    q.append(n)
                clones[curr].neighbors.append(clones[n])
        return clones[node]






