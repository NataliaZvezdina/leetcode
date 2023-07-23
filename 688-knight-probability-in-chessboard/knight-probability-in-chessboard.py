class Solution:    

    def knightProbability(self, n: int, moves: int, r: int, c: int) -> float:
        mp = {}
        dir = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        
        return self.find(n, moves, r, c, mp, dir)


    def find(self, n: int, moves: int, r: int, c: int, mp, dir) -> float:
        if r < 0 or r >= n or c < 0 or c >= n:
            return 0

        if moves == 0:
            return 1
    
        key = f'{r} {c} {moves}'
        if key in mp:
            return mp[key]

        probability = 0
        for i in range(8):
            probability += self.find(n, moves - 1, r+dir[i][0], c+dir[i][1], mp, dir) / 8
            
        mp[key] = probability
        return mp[key]
        