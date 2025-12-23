from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums) # 把 nums 转为哈希集合
        ans = 0
        for x in st: # 遍历哈希集合
            if x - 1 in st: # 如果 x 不是连续序列的起点，跳过
                continue
            y= x + 1  # 寻找以 x 为起点的最长连续序列
            while y in st: # 不断地向后寻找下一个数是否在哈希集合中
                y += 1
            # 循环结束，y - 1 是最后一个在哈希集合种的数
            ans = max(ans, y-x)
        return ans
    