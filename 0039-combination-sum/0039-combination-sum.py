class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []


        self.solve(candidates,target,0,[],ans)
        return ans


    def solve(self,candidates,target,i,temp,ans):
        if i == len(candidates):
            if target  == 0:
                ans.append(temp[:])
            return
                
            
            
        
        if candidates[i] <= target:
            temp.append(candidates[i])
            self.solve(candidates,target-candidates[i],i,temp,ans)
            temp.pop()

        self.solve(candidates,target,i+1,temp,ans)

            
        


       
        