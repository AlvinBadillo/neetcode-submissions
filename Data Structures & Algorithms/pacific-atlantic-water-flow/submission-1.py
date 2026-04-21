class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(row, col, ocean, prevH):
            # I want to add all the coordinates to the set if I can reach that cell
            # Since we are going from ocean to land, instead of lan to ocean we have to inverse how we can move
            # It will be allowed to go on if the height of the previous land is smaller than curr
            
            # Base case 1: Out of bounds, return
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            # Not valid since prevH > curr height
            if prevH > heights[row][col]:
                return
            # If coords already in the set
            if (row, col) in ocean:
                return 
        
            # If none those conditions are met, add the coords to ocean set
            ocean.add((row, col))
            
            dfs(row + 1, col, ocean, heights[row][col])
            dfs(row - 1, col, ocean, heights[row][col])
            dfs(row, col + 1, ocean, heights[row][col])
            dfs(row, col - 1, ocean, heights[row][col])

        ROWS, COLS = len(heights), len(heights[0])
        # Perform dfs from pacific rows to atlantic and from atlantic to pacific
        # Create two sets, one to hold the ones that reach pacific and another than can reach the atlantic
        # At the end return the cells that are in both
        
        # Declare sets
        atl, pac = set(), set()

        # Perform dfs top and bottom
        for col in range(COLS):
            # Top row
            dfs(0, col, pac, heights[0][col])
            # pac.add((0, col))
            # Bottom row
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])
            # atl.add((ROWS -1, col))
        # Perform dfs for left and right cols
        for row in range(ROWS):
            # Left col
            dfs(row, 0, pac, heights[row][0])
            # pac.add((row, 0))
            # Right col
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])
            # atl.add((row, COLS - 1))
            
        resultSet = atl.intersection(pac)
        return [list(item) for item in resultSet]





