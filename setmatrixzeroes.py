class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_length = len(matrix[0])
        row_length = len(matrix)
        row_1 = False
        for r in range(row_length):
            for c in range(col_length):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        row_1 = True
                    else:
                        matrix[r][0] = 0
        for r in range(1, row_length):
            for c in range(1, col_length):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(row_length):
                matrix[r][0] = 0

        if row_1:
            for c in range(col_length):
                matrix[0][c] = 0  
