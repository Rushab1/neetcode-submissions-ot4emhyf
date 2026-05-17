class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if n == 0:
                    grid[i][j] = max(grid[i][j-1], grid[i][j])

                elif m == 0:
                    grid[i][j] = max(grid[i-1][j], grid[i][j])
                
                else:
                    grid[i][j] = min(max(grid[i-1][j], grid[i][j]), max(grid[i][j-1], grid[i][j]))

        return grid[-1][-1]
                