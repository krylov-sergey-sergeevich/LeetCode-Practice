# https://leetcode.com/problems/get-equal-substrings-within-budget
# Medium
from src.AssertUtils import check


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        data = [0] * len(s)
        for i in range(len(s)):
            data[i] = abs(ord(s[i]) - ord(t[i]))
        # print(data)
        l = 0
        draft_max = 0
        draft_count = 0
        result_count = 0
        for i in range(len(data)):
            if draft_max <= maxCost:
                draft_max += data[i]
                draft_count += 1
                # print(f"Plus: {draft_max} | {draft_count}")
            if draft_max > maxCost:
                j = l
                while draft_max > maxCost:
                    draft_max -= data[j]
                    draft_count -= 1
                    # print(f"Minus: {draft_max} | {draft_count}")
                    j += 1
                l = j
            if draft_count != 0 and draft_max <= maxCost:
                result_count = max(result_count, draft_count)
                # print(f"set result_count={result_count}")

        return result_count


if __name__ == '__main__':
    solution = Solution()
    check(solution.equalSubstring("abcd", "bcdf", 3), 3)
    check(solution.equalSubstring("abcd", "cdef", 3), 1)
    check(solution.equalSubstring("abcd", "acde", 0), 1)
    check(solution.equalSubstring("abcd", "cdef", 1), 0)
    check(solution.equalSubstring("krrgw", "zjxss", 19), 2)
    check(solution.equalSubstring("anryddgaqpjdw", "zjhotgdlmadcf", 5), 1)
