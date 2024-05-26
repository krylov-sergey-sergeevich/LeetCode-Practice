# https://leetcode.com/problems/sum-of-all-subset-xor-totals
# Easy
from typing import List


class Solution:

    def subSetXOR(self, data: List[int], nums: List[int]):
        if len(nums) == 0:
            if len(data) == 0:
                return 0
            else:
                res = data[0]
                for i in range(1, len(data)):
                    res = res ^ data[i]
                return res
        else:
            data_new1 = data.copy()
            data_new2 = data.copy()
            nums_new = nums.copy()
            element = nums_new.pop()
            data_new1.append(element)
            return self.subSetXOR(data_new1, nums_new) + self.subSetXOR(data_new2, nums_new)

    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        return self.subSetXOR([], nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetXORSum([1, 3]))
    print(solution.subsetXORSum([5, 1, 6]))
