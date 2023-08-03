class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(curr, remain, start):
            if remain < 0: return
            if remain == 0:
                res.append(curr[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]: continue
                curr.append(candidates[i])
                backtrack(curr, remain-candidates[i], i+1)
                curr.pop()
                
        res = []
        candidates.sort()
        backtrack([], target, 0)
        return res