class Solution(object):
    def permute(self, nums):
        ans = []
        self.solve(nums, [],ans)
        return ans
    def solve(self,nums,temp,ans):
        if len(temp) == len(nums):
            ans.append(temp[:])
            return
        for i in nums:
            if i not in temp:
                temp.append(i)
                self.solve(nums,temp,ans)
                temp.pop()
            

       
        