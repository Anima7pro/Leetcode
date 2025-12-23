from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0
        for x in range(1, target[-1]+1):
            ans.append("Push")
            if x == target[i]:
                i += 1
            else:
                ans.append("Pop")
        return ans
        
""" 
https://leetcode.cn/problems/build-an-array-with-stack-operations/description/

看示例 1，n=3 意味着我们会依次读取 1,2,3 这三个数。

1 在 target 中，入栈。
2 不在 target 中，先入栈，再出栈。注意一定要入栈，这是题目要求。
3 在 target 中，入栈。现在栈等于 target。
怎么判断当前读取的数是否在 target 中？

设 target 的最后一个数为 mx。初始化指针 i = 0，指向 target 的第一个数。
枚举读取的数为 x=1, 2, … , mx。
先把 x 入栈。
如果 x = target[i]，那么 x 是我们要的数，把 i 加一，指向 target 的下一个数。
否则 x < target[i]，那么 x 不是我们要的数，把 x 出栈。
由于 target 是严格递增的，所以 x ≤ target[i] 始终成立。


"""