class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Graph representation
        classPreR = [[] for _ in range(numCourses)]
        # Fill out classPreR
        for course, preR in prerequisites:
            classPreR[course].append(preR)

        # Set to keep track of visited node to detect a loop
        visited = set()  
        def dfs(curr):
            if curr in visited:
                return False
            # visited.add(curr) -> if i have this line here it does not work
            # Base case where list is empty
            if classPreR[curr] == []:
                return True
            visited.add(curr) # But here it works 
            # If not, run dfs on all of curr preReq
            for preR in classPreR[curr]:
                if not dfs(preR):
                    return False
            # If we have reached this point in the code it means that curr cam be completed
            # Set the list of preR for curr to empty as we know it can be completed
            classPreR[curr] = []
            # remove curr from visited 
            visited.remove(curr)
            return True
        # Run dfs on all nodes
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            
