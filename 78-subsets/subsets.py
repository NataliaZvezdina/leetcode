class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i=0, curr=[]):
             output.append(curr[:])
             
             for idx in range(i, len(nums)):
                 curr.append(nums[idx])
                 backtrack(idx+1, curr)
                 curr.pop()


        output = []
        backtrack()
        return output
