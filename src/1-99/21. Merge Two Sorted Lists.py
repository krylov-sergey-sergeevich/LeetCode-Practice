from typing import Optional

"""
https://leetcode.com/problems/merge-two-sorted-lists/

21. Merge Two Sorted Lists
21. Объединение двух списков
Easy
Accepted

Time: O(n)
Space: O(1)
"""


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pred_cursor = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                pred_cursor.next = list1
                list1, pred_cursor = list1.next, list1
            else:
                pred_cursor.next = list2
                list2, pred_cursor = list2.next, list2

        if list1 or list2:
            pred_cursor.next = list1 if list1 else list2

        return head.next


if __name__ == "__main__":
    pass
