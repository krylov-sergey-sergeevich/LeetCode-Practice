from typing import List

from src.AssertUtils import check

"""
https://leetcode.com/problems/verifying-an-alien-dictionary/

953. Verifying an Alien Dictionary
Easy
Accepted
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)):
            word = words[i]
            for j in range(i + 1, len(words)):
                compWord = words[j]
                t = 0
                while True:
                    i1 = self.idx(word[t], order)
                    i2 = self.idx(compWord[t], order)
                    # print("t " + str(t))
                    # print("i1 " + str(i1) + " " + word[t] + " " + word)
                    # print("i2 " + str(i2) + " " + compWord[t] + " " + compWord)
                    if i2 > i1:
                        break
                    elif i1 > i2:
                        return False
                    else:
                        if t + 1 == len(word):
                            break
                        elif t + 1 == len(compWord):
                            return False
                        else:
                            t += 1
        return True

    def idx(self, symbol: str, order: str) -> int:
        return order.find(symbol)


class BestSolution:
    order_map = [0] * 26

    def isAlienSorted(self, words, order):
        for i in range(len(order)):
            self.order_map[ord(order[i]) - ord('a')] = i

        for i in range(1, len(words)):
            if not self.compare(words[i], words[i - 1]):
                return False
        return True

    def compare(self, s1, s2):
        j = 0
        while j < len(s1) and j < len(s2):
            if s1[j] == s2[j]:
                j += 1
            elif self.order_map[ord(s1[j]) - ord('a')] > self.order_map[ord(s2[j]) - ord('a')]:
                return True
            else:
                return False
        if len(s1) < len(s2):
            return False
        return True


if __name__ == "__main__":
    solution = Solution()

    check(solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True)
    check(solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"), False)
    check(solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"), False)
    check(solution.isAlienSorted(
        ["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve", "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge",
         "qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"), False)

    solution = BestSolution()

    check(solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True)
    check(solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"), False)
    check(solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"), False)
    check(solution.isAlienSorted(
        ["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve", "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge",
         "qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"), False)
