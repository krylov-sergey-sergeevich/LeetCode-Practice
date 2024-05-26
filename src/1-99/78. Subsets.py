# https://leetcode.com/problems/subsets/
# Easy
from typing import List


class Solution:

    def remove_duplicates(self, arrays):
        seen = set()
        unique_arrays = []
        for array in arrays:
            # Преобразуем список в кортеж, чтобы можно было использовать его в множестве
            array_tuple = tuple(array)
            if array_tuple not in seen:
                seen.add(array_tuple)
                unique_arrays.append(array)
        return unique_arrays

    def generate_combinations(self, arr):
        n = len(arr)
        result = []
        for i in range(0, 2 ** n):
            combination = []
            for j in range(n):
                if i & (1 << j):
                    combination.append(arr[j])
            result.append(combination)
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = self.generate_combinations(nums)
        return self.remove_duplicates(combinations)


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
    assert solution.subsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert solution.subsets([0]) == [[], [0]]
