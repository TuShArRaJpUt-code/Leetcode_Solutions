class Solution(object):
    def climbStairs(self, n):
        dp=[-1]*(n+1)
        return self.ways(n,dp)
    def ways(self,n,dp):
        if n ==1:
            return 1
        if n == 2:
            return 2
        if dp[n] != -1:
            return dp[n]
        dp[n] =  self.ways(n-1,dp)+self.ways(n-2,dp)
        return dp[n]

       
       
        