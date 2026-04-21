class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        grid = [[1] * n] * m
        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row- 1][col] + grid[row][col - 1]
        return grid[m-1][n-1]