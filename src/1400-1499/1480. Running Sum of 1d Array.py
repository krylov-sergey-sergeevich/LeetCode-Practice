from typing import List

from src.AssertUtils import check

"""
https://leetcode.com/problems/running-sum-of-1d-array/

1480. Running Sum of 1d Array
Easy
Accepted
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        s = 0
        for el in nums:
            s += el
            result.append(s)
        return result


if __name__ == "__main__":
    solution = Solution()

    check(solution.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])
    check(solution.runningSum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])
    check(solution.runningSum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])
