class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        def find_in_row(arr):
            left, right = 0, cols-1
            while left <= right:
                mid = (left+right) // 2
                if target > arr[mid]:
                    left = mid+1
                elif target < arr[mid]:
                    right = mid-1
                else:
                    return True
            
            return False

        low, high = 0, rows-1
        while low <= high:
            mid = (low+high) // 2
            if target > matrix[mid][-1]:
                low = mid+1
            elif target < matrix[mid][0]:
                high = mid-1
            else:
                if find_in_row(matrix[mid]):
                    return True
                else:
                    del matrix[mid]
                    high -= 1
        
        return False
