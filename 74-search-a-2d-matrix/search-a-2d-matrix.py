class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        low, high = 0, rows-1
        
        while low <= high:
            mid_row = (low+high) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][cols-1]:                
                break
            elif target > matrix[mid_row][cols-1]:
                low = mid_row+1
            else:
                high = mid_row-1

        if not low <= high: 
            return False
        
        left, right = 0, cols-1
        mid_row = (low+high) // 2
        while left <= right:
            mid = (left+right) // 2
            if matrix[mid_row][mid] == target:                        
                return True
            elif target > matrix[mid_row][mid]:
                left = mid+1
            else:
                right = mid-1

        return False
