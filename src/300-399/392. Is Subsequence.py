from src.AssertUtils import check

"""
https://leetcode.com/problems/is-subsequence

392. Is Subsequence
Easy
Accepted
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = "".join(list(filter(lambda it: it in s, t)))
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            if s[i] in t:
                index = t.index(s[i]) + 1
                t = t[index:]
                # print(t)
            else:
                return False
        return True


class BestSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # По сути два индекса
        sl, tl = 0, 0
        while sl < len(s) and tl < len(t):
            if s[sl] == t[tl]:
                sl += 1
                tl += 1
            else:
                tl += 1
        if sl == len(s):
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()

    check(solution.isSubsequence("abc", "ahbgdc"), True)
    check(solution.isSubsequence("axc", "ahbgdc"), False)
    check(solution.isSubsequence("aaaaaa", "bbaaaa"), False)
    check(solution.isSubsequence("ace", "abcde"), True)
    check(solution.isSubsequence("ace", "aec"), False)
    check(solution.isSubsequence("leeeeetcode", "leeeeeetcode"), True)
    check(solution.isSubsequence("rjufvjafbxnbgriwgokdgqdqewn",
                                 "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq"),
          False)

    solution = BestSolution()

    check(solution.isSubsequence("abc", "ahbgdc"), True)
    check(solution.isSubsequence("axc", "ahbgdc"), False)
    check(solution.isSubsequence("aaaaaa", "bbaaaa"), False)
    check(solution.isSubsequence("ace", "abcde"), True)
    check(solution.isSubsequence("ace", "aec"), False)
    check(solution.isSubsequence("leeeeetcode", "leeeeeetcode"), True)
    check(solution.isSubsequence("rjufvjafbxnbgriwgokdgqdqewn",
                                 "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq"),
          False)
