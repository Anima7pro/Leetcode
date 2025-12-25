from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix) # 行数
        n = len(matrix[0]) # 列数
        set_m = set()
        set_n = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_m.add(i)
                    set_n.add(j)
        for i in set_m:
            matrix[i][:] = [0] * n  

        # 2. 处理所有需要置零的列
        for j in set_n:
            for r in range(m):      
                matrix[r][j] = 0
                
        """
        Do not return anything, modify matrix in-place instead.
        """
        
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        row_has_zeros = [0 in row for row in matrix]
        col_has_zeros = [0 in col for col in zip(*matrix)]
        
        for i, row0 in enumerate(row_has_zeros):
            for j, col0 in enumerate(col_has_zeros):
                if row0 or col0:
                    matrix[i][j] = 0
                    
        
        