class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list representation of the graph
        graph = {i:[] for i in range(n)}
        for edge in edges:
            left = edge[0]
            right = edge[1]
            graph[left].append(right)
            graph[right].append(left)

        # We know we have n nodes from 0 to n-1
        # We need to detect if there are edges that are not conected in the same edge conection
        # Set up set will all nodes we have to visit
        toVisit = set()
        for node in range(n):
            toVisit.add(node)

        def dfs(node):
            toVisit.remove(node)
            # Call dfs on all neighbors of curr node
            for n in graph[node]:
                if n in toVisit:
                    dfs(n)
        
        result = 0
        for node in range(n):
            if node in toVisit:
                # This function will iterate the conected portion of the node and remove them from the set as it goes
                # Also counting the amount of nodes
                dfs(node)
                result += 1
        return result
                
    















