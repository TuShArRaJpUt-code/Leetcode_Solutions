class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n=len(text2)
        dp=[[-1]*(n+1) for _ in range(m+1)]
        return self.solve(text1,text2,m,n,dp)
    def solve(self,a,b,i,j,dp):
        if i == 0 or j ==0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if a[i-1] == b[j-1]:
           dp[i][j] =  1+self.solve(a,b,i-1,j-1,dp)
        else:
            dp[i][j]= max(
            self.solve(a,b,i-1,j,dp),
            self.solve(a,b,i,j-1,dp)
            )
        return dp[i][j]
           


        