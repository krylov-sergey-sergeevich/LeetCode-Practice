from typing import Optional

"""
https://leetcode.com/problems/reverse-linked-list

206. Reverse Linked List
Easy
Accepted
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = None
        while head:
            pred_node = cursor
            next_node = head.next
            cursor = head
            cursor.next = pred_node
            head = next_node
        return cursor


# По времени решение которые выше быстрее оказалось
class BestSolution:
    def reverseList(self, head):
        # Initialize prev pointer as NULL...
        prev = None
        # Initialize the curr pointer as the head...
        curr = head
        # Run a loop till curr points to NULL...
        while curr:
            # Initialize next pointer as the next pointer of curr...
            next = curr.next
            # Now assign the prev pointer to curr’s next pointer.
            curr.next = prev
            # Assign curr to prev, next to curr...
            prev = curr
            curr = next
        return prev  # Return the prev pointer to get the reverse linked list...


if __name__ == "__main__":
    solution = Solution()
