class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i=0, curr=[]):
            output.append(curr[:])
            
            for idx in range(i, len(nums)):
                if idx > i and nums[idx] == nums[idx-1]: continue
                curr.append(nums[idx])
                backtrack(idx+1, curr)
                curr.pop()
        
        nums.sort()
        output = []
        backtrack()
        return output
