from typing import List

from src.AssertUtils import check

"""
https://leetcode.com/problems/find-pivot-index

724. Find Pivot Index
Easy
Accepted
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        seqSum = 0
        for i in range(len(nums)):
            if s - nums[i] - seqSum == seqSum:
                return i
            seqSum += nums[i]
        return -1


if __name__ == "__main__":
    solution = Solution()

    check(solution.pivotIndex([1, 7, 3, 6, 5, 6]), 3)
    check(solution.pivotIndex([1, 2, 3]), -1)
    check(solution.pivotIndex([2, 1, -1]), 0)
    check(solution.pivotIndex([-1, -1, -1, 1, 1, 1]), -1)
