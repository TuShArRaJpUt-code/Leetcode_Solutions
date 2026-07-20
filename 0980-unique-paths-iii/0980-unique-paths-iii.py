class Solution(object):
    def uniquePathsIII(self, grid):

        m = len(grid)
        n = len(grid[0])

        start_x = start_y = 0
        empty = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    empty += 1
                if grid[i][j] == 1:
                    start_x, start_y = i, j
        return self.dfs(grid, start_x, start_y, empty)

    def dfs(self, grid, i, j, remain):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if grid[i][j] == -1:
            return 0

        if grid[i][j] == -1:
             return 0

        if grid[i][j] == 2:
             return 1 if remain == 1 else 0

        temp = grid[i][j]
        grid[i][j] = -1

        paths = (
             self.dfs(grid, i+1, j, remain-1) +
             self.dfs(grid, i-1, j, remain-1) +
             self.dfs(grid, i, j+1, remain-1) +
             self.dfs(grid, i, j-1, remain-1) 
             )

        grid[i][j] = temp
        return paths

   
    
    
    

   


        
        