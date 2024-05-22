# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, nums, slate, output):
            if i == len(nums):
                output.append(slate[:])
                return
                
            
            dfs(i + 1, nums, slate, output)
            slate.append(nums[i])
            dfs(i + 1, nums, slate, output)
            slate.pop()
        
        output = []
        dfs(0, nums, [], output)
        return output

        
       

