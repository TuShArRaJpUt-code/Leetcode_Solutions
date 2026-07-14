class Solution(object):
    def combinationSum2(self, candidates, target):

        candidates.sort()
        ans = []
        self.solve(candidates,target,0,[],ans)
        return ans
    
    def solve(self, candidates , target ,i,  temp, ans):
        if i == len(candidates):
            if target  == 0:
                ans.append(temp[:])
            return

        if candidates[i] <= target:
            temp.append(candidates[i])
            self.solve(candidates,target-candidates[i],i+1,temp,ans)
            temp.pop()
            while i +1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

        self.solve(candidates,target,i+1,temp,ans)

        