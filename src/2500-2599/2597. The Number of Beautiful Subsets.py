from typing import List

# 1 2 3 7 k=5

abs(1 + 5)
abs(1 - 5)


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        result = [0]  # Используем список для изменения значения внутри вложенной функции

        def dfs(branch: set[int], data: List[int]):
            if len(data) == 0:
                if len(branch) != 0:
                    result[0] += 1
                return
            x = data[0]
            if x in branch:
                dfs(branch, data[1:])
                return
            else:
                new_branch = branch.copy()
                branch.add(x + k)
                if x - k > 0:
                    branch.add(x - k)
                dfs(new_branch, data[1:])
                dfs(branch, data[1:])

        dfs(set(), nums)
        return result[0]


if __name__ == '__main__':
    solution = Solution()
    assert solution.beautifulSubsets([2, 4, 6], 2) == 4
    assert solution.beautifulSubsets([1], 1) == 1
    print(solution.beautifulSubsets(
        [686, 729, 872, 547, 443, 50, 746, 13, 102, 548, 158, 155, 73, 114, 77, 204, 544, 956, 484, 565], 101))
    assert solution.beautifulSubsets(
        [686, 729, 872, 547, 443, 50, 746, 13, 102, 548, 158, 155, 73, 114, 77, 204, 544, 956, 484, 565], 101
    ) == 786431
