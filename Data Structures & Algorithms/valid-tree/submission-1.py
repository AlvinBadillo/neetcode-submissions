class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Set up adjacency dict
        graph = {i: [] for i in range(n)}
        for edge in edges:
            # Add index 1 to value of index 0
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(node, prevNode):
            visited.add(node)
            # Check if we found a loop by checking if any of the neighbors have been visited and are not prevNode
            for n in graph[node]:
                if n == prevNode:
                    continue
                if n in visited:
                    return False
                # If its valid, call dfs on its neighbors
                if dfs(n, node) == False:
                    return False
            return True

        if dfs(0, -1) == False:
            return False
        # Check if visited len is the same as n
        return n == len(visited)
