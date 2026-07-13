class Solution(object):
    def subsets(self, nums):
     
        
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
        self.solve(nums,i+1,temp,ans)

        
        