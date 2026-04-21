class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_map = grid
        traker = 2

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    # Perform BFS
                    self.island_map = self.mark_island(grid, traker, row, col)
                    traker += 1
        return traker - 2

    def mark_island(self, island_map: List[List[str]], traker, row, col):
        if 0 <= row < len(island_map) and 0 <= col < len(island_map[0]) and island_map[row][col] and island_map[row][col] == "1":
            island_map[row][col] = str(traker)
            # Search above
            self.mark_island(island_map, traker, row + 1, col)
            # Search below
            self.mark_island(island_map, traker, row - 1, col)
            # Search right
            self.mark_island(island_map, traker, row, col + 1)
            # Search left
            self.mark_island(island_map, traker, row, col - 1)




