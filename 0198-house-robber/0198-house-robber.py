class Solution(object):
    def rob(self, nums):
        n=len(nums)

        if n == 1:
            return nums[0]
        dp = [-1]*(n+1)
        return self.solve(nums,n-1,dp)
    def solve(self,nums,idx,dp):
        if idx == 0:
            return nums[0]
        if idx == 1 :
            return max(nums[0],nums[1])
        if dp[idx] != -1:
            return dp[idx]
        rob = nums[idx] + self.solve(nums,idx-2,dp)
        noRob =  self.solve(nums,idx-1,dp)
        dp[idx] =  max(rob,noRob)
        return dp[idx]

        
        