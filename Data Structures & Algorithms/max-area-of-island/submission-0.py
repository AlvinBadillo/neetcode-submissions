class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def find_area(row, col):
            if row < 0 or row >= len(grid) or col >= len(grid[0]) or col < 0 or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            area = 1
            area += find_area(row + 1, col)
            area += find_area(row - 1, col) 
            area += find_area(row, col + 1)
            area += find_area(row, col - 1)
            return area
            

        maxArea = 0
        # Iterate the entire grid and everytime we find a 1, serach all neighboring cells
        # Everytime we find a 1 caluculate the area of that island
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr = grid[row][col]
                if curr == 1:
                    maxArea = max(maxArea, find_area(row, col))
        return maxArea