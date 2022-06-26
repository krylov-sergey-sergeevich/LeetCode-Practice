from collections import Counter
from typing import List

# Status: Accepted
# https://leetcode.com/submissions/detail/731643296/
# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        counts = dict()
        for i in items:
            counts[i] = counts.get(i, 0) + 1
        """
        store = Counter(nums)
        for i in range(len(nums)):
            findElement = target - nums[i]
            bucket = store.get(findElement, 0)
            if bucket > 0:
                if nums[i] != findElement:
                    for j in range(i + 1, len(nums)):
                        if nums[j] == findElement:
                            return [i, j]
                else:
                    if store.get(findElement) > 1:
                        for j in range(i + 1, len(nums)):
                            if nums[j] == findElement:
                                return [i, j]


if __name__ == '__main__':
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
