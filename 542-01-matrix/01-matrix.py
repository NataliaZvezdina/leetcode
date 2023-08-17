class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        ans = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i,j))

        while q:
            i, j = q.popleft()

            if 0 <= i+1 < len(mat) and 0 <= j < len(mat[0]) and ans[i+1][j] == -1:
                q.append((i+1,j))
                ans[i+1][j] = ans[i][j] + 1
            
            if 0 <= i-1 < len(mat) and 0 <= j < len(mat[0]) and ans[i-1][j] == -1:
                q.append((i-1,j))
                ans[i-1][j] = ans[i][j] + 1

            if 0 <= i < len(mat) and 0 <= j+1 < len(mat[0]) and ans[i][j+1] == -1:
                q.append((i,j+1))
                ans[i][j+1] = ans[i][j] + 1

            if 0 <= i < len(mat) and 0 <= j-1 < len(mat[0]) and ans[i][j-1] == -1:
                q.append((i,j-1))
                ans[i][j-1] = ans[i][j] + 1        

        return ans
