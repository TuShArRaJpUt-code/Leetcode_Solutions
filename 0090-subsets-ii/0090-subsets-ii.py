class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        self.solve(nums,0,[],ans)
        return ans
    def solve(self,nums,i,temp,ans):
        if i == len(nums):
            ans.append(temp[:])
            return
        temp.append(nums[i])
        self.solve(nums,i+1,temp,ans)
        temp.pop()
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1

    
        self.solve(nums,i+1,temp,ans)

       
        