def isAnagram(s, t):
    if len(s) != len(t):
        return False
    for idx in set(s):
        if s.count(idx) != t.count(idx):
            return False
    return True


class Solution(object):
    def findAnagrams(self, s, t):
        l = len(t)
        result = []
        for idx in range(len(s) - l + 1):
            if isAnagram(s[idx:idx + l], t):
                result.append(idx)
        return result


if __name__ == '__main__':
    solution = Solution()

    print(solution.findAnagrams("cbaebabacd", "abc"))
    print(solution.findAnagrams("abab", "ab"))
