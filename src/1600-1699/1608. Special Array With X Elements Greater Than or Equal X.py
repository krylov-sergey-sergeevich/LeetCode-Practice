# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
# Easy

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        def is_approach(x, data):
            count = 0
            for el in data:
                if el >= x:
                    count += 1
            return x == count

        for el in range(1, nums[-1]):
            if is_approach(el, nums):
                return el
        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.specialArray([0, 4, 3, 0, 4]) == 3
    assert solution.specialArray([1, 0, 0, 6, 4, 9]) == 3
    assert solution.specialArray([3, 5]) == 2
    assert solution.specialArray([0, 0]) == -1
