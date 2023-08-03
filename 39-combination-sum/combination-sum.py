class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(curr, remain, start):
            if remain < 0: return
            if remain == 0: 
                res.append(curr[:])
                return
            
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(curr, remain-candidates[i], i)
                curr.pop()

        res = []
        backtrack([], target, 0)
        return res