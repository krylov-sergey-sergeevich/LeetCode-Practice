from src.AssertUtils import check

"""
https://leetcode.com/problems/isomorphic-strings

205. Isomorphic Strings
Easy
Accepted
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        d = dict()
        for idx in range(len(s)):
            if s[idx] in d and d[s[idx]] == t[idx]:
                pass
            elif s[idx] in d and d[s[idx]] != t[idx]:
                # print(f"{d}")
                # print(f"{s[idx]} - {t[idx]}")
                return False
            else:
                d[s[idx]] = t[idx]
        return True


if __name__ == "__main__":
    solution = Solution()

    check(solution.isIsomorphic("egg", "add"), True)
    check(solution.isIsomorphic("foo", "bar"), False)
    check(solution.isIsomorphic("paper", "title"), True)
    check(solution.isIsomorphic("badc", "baba"), False)
