# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        sum_l1 = sum_l2 = 0
        cnt_1 = cnt_2 = 0
        while l1:
            sum_l1 += l1.val * (10 ** cnt_1)
            l1 = l1.next
            cnt_1 += 1
        while l2:
            sum_l2 += l2.val * (10 ** cnt_2)
            l2 = l2.next
            cnt_2 += 1
        sum_total = sum_l1 + sum_l2
        result = dummy = ListNode() # type: ignore
        if sum_total == 0:
            result.next = ListNode(0) # type: ignore
            return dummy.next
        while sum_total / 10:
            result.next = ListNode(sum_total % 10) # type: ignore
            sum_total = sum_total // 10
            result = result.next
        return dummy.next
        