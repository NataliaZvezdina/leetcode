class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        mp = defaultdict(int)
        res = []
        for num in nums:
            row = mp[num]
            if row == len(res):
                res.append([])
            res[row].append(num)
            mp[num] += 1        
        
        return res
