from src.AssertUtils import check

"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/

1071. Greatest Common Divisor of Strings
Easy
Accepted
"""


def check_completely_cut(base_str, cut_str) -> bool:
    s1, s2 = max(base_str, cut_str), min(base_str, cut_str)
    i = 0
    l1 = len(s1)
    j = 0
    l2 = len(s2)
    while True:
        if s1[i] != s2[j]:
            return False
        else:
            if l1 == i + 1:
                i += 1
                j += 1
                break
            if l2 == j + 1:
                j = -1
        i += 1
        j += 1
    if i == l1 and j == l2:
        return True
    else:
        return False


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1, s2 = max(str1, str2), min(str1, str2)
        i = 0
        l1 = len(s1)
        j = 0
        l2 = len(s2)
        while True:
            if s1[i] != s2[j]:
                return ""
            else:
                if l1 == i + 1:
                    i += 1
                    j += 1
                    break
                if l2 == j + 1:
                    j = -1
            i += 1
            j += 1
        div = s2[:j]
        if j != l2:
            for i in range(len(div) - 1, 0, -1):
                if check_completely_cut(div, div[:i]) and check_completely_cut(s1, div[:i]) \
                        and check_completely_cut(s2, div[:i]):
                    return div[:i]
        r1 = check_completely_cut(s1, div)
        r2 = check_completely_cut(s2, div)
        # print("div " + div)
        if r1 and r2:
            return div
        else:
            return ""


"""
GCD - Наибольший общий делитель строк.
"""


class BestSolution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        if str1 == str2:
            return str1
        if str1[:len(str2)] != str2:
            return ""
        return self.gcdOfStrings(str1[len(str2):], str2)


if __name__ == "__main__":
    solution = Solution()

    check(solution.gcdOfStrings("ABCABC", "ABC"), "ABC")
    check(solution.gcdOfStrings("ABCABCA", "ABC"), "")
    check(solution.gcdOfStrings("ABABAB", "ABAB"), "AB")
    check(solution.gcdOfStrings("LEET", "CODE"), "")
    check(solution.gcdOfStrings("AAA", "AAA"), "AAA")
    check(solution.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"), "TAUXX")
    check(solution.gcdOfStrings(
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"),
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
