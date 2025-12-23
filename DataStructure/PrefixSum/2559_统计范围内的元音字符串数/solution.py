from itertools import accumulate
from typing import List


def f (words: List[str]) ->List[int]:
    condition = {'a','e','i','o','u'}
    result = []
    for i, word in enumerate(words):
        if word[0] in condition and word[-1] in condition:
            result.append(1)
        else:
            result.append(0)
    return list(accumulate(result, initial = 0))
            

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        s = f(words)
        for l, r in queries:
            result.append(s[r+1]-s[l])
        return result

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = list(accumulate((w[0] in "aeiou" and w[-1] in "aeiou" for w in words), initial=0))
        return [s[r + 1] - s[l] for l, r in queries]


        