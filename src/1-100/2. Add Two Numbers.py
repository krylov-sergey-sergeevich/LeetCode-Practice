# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Status: -
# h
# https://leetcode.com/problems/add-two-numbers/
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode
        a = l1
        b = l2
        value = 0
        inc = 0
        hasNext = True
        while hasNext:
            hasNext = False
            value = 0
            if a is not None:
                if a.next is not None:
                    hasNext = True
                    a = a.next
            if b is not None:
                if b.next is not None:
                    hasNext = True
                    b = b.next

            result.val = value % 10 + inc
            if value > 10:
                inc = 1
            else:
                inc = 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.addTwoNumbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]
    assert solution.addTwoNumbers([0], [0]) == [0]
    assert solution.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [8, 9, 9, 9, 0, 0, 0, 1]
