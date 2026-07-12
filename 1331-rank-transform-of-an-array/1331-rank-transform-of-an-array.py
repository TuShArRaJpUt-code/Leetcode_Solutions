class Solution(object):
    def arrayRankTransform(self, arr):
       sorted_arr = sorted(set(arr))

       rank={}
       for i , num in enumerate(sorted_arr):
        rank[num] = i+1
       return [rank[num] for num in arr]
        
