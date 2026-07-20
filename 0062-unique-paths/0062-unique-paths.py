class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[-1]*(n+1)for _ in range(m+1)]
        return self.solve(m, n,dp)

    def solve(self, m, n,dp):
        if m == 1 and n == 1:
            return 1

        if m == 0 or n == 0:
            return 0
        
        if dp[m][n] != -1:
            return dp[m][n]

        dp[m][n] = self.solve(m - 1, n,dp) + self.solve(m, n - 1,dp)
        return dp[m][n]
      