class Solution(object):
    def numDistinct(self, s, t):
        m=len(s)
        n=len(t)
        dp = [[-1]*(n+1)for _ in range(m+1)]
        return self.solve(s,t,m,n,dp)
    def solve(self,s,t,i,j,dp):
        if j == 0:
            return 1
        if i == 0:
            return 0
        
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i-1] != t[j-1]:
            dp[i][j] = self.solve(s,t,i-1,j,dp)
        else:

            dp[i][j] = self.solve(s,t,i-1,j-1,dp) + self.solve(s,t,i-1,j,dp)
                
            
        return dp[i][j]
            
        
        

        
        