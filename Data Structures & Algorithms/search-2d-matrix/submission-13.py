class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        
        l,r = 0, len(matrix)-1

        row = 0
        m=0
        while l <= r:
            m = (r+l) // 2
            if target < matrix[m][0]:
                r = m-1
            elif target > matrix[m][-1]:
                l = m+1
            else:
                break
        
        row = m
        
        l,r = 0, len(matrix[0])-1

        while l <= r:
            m = (r+l) // 2
            if target < matrix[row][m]:
                r = m-1
            elif target > matrix[row][m]:
                l = m+1
            else:
                return True
        
        return False
          

        
        