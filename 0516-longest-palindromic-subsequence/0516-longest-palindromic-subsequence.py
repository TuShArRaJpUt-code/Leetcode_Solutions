class Solution(object):
    def longestPalindromeSubseq(self, s):
        m = len(s)
        a=s
        b=s[::-1]
        dp=[[-1]*(m+1) for _ in range(m+1)]
        return self.solve(a,b,m,m,dp)
    def solve(self,a,b,i,j,dp):
        if i == 0 or j==0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if a[i-1] == b[j-1]:
            dp[i][j] = 1+ self.solve(a,b,i-1,j-1,dp)
        else:
            dp[i][j] = max(
                self.solve(a,b,i-1,j,dp),
                self.solve(a,b,i,j-1,dp)
            )
        return dp[i][j]

        
        