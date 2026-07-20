class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*(n+1)for _ in range(m+1)]
        
        return self.solve(m-1, n-1,obstacleGrid,dp)

    def solve(self, i, j, grid, dp):
        if i < 0 or j < 0:
            return 0
        

        if grid[i][j] == 1:
            return 0
        

        if i == 0 and j == 0:
            return 1
        

        if dp[i][j] != -1:
            return dp[i][j]
        

        dp[i][j] = self.solve(i - 1, j, grid, dp) + self.solve(i, j - 1, grid, dp)

        return dp[i][j]


    

    

    

    

    

   
        