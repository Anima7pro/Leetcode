from typing import List


DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)

# 每次移动相当于把行号增加DIRS[di][0], 列号增加DIRS[di][1]
# 向右转90度 相当于把di增加1，但在di = 3 时要回到di = 0 即 （di+1）%4
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        i = j = di = 0
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = None
            x, y = i + DIRS[di][0], j + DIRS[di][1]
            if x < 0 or x >= m or j < 0 or j >= n or matrix[x][y] is None:
                di = (di + 1) % 4
            i += DIRS[di][0]
            j += DIRS[di][1]
        return ans

    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        size = m * n
        ans = []
        i, j, di = 0, -1, 0
        while (len(ans)) < size:
            dx, dy = DIRS[di]
            for _ in range(n): # 步数根据方向不同会变换
                i += dx
                j += dy
                ans.append(matrix[i][j])
            di = (di + 1) % 4
            n, m = m-1, n # 循环，使其螺旋变换
        return ans
""" 
https://leetcode.cn/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-100-liked

从(0, -1)开始，向右走 n 步 ，向下走 m - 1 步， 向左走 n - 1 步， 向上走 m - 2 步 向右走 n -2 步

简化：
n, m = m - 1, n
第一次走 n 步
第二次走 n = m - 1 步
第三次走 n = n - 1 步
第四次走 n = m - 2 步
"""