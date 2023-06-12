"""
https://leetcode.com/problems/summary-ranges/

228. Summary Ranges
Easy
Accepted
20 minutes | 1 попытка
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        nums.append(nums[0])
        result = []
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i] - 1:
                if prev == nums[i - 1]:
                    result.append(str(prev))
                else:
                    result.append(f"{prev}->{nums[i - 1]}")
                prev = nums[i]
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
    print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))

