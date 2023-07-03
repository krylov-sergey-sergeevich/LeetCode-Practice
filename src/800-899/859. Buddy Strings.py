"""
https://leetcode.com/problems/buddy-strings

859. Buddy Strings
Easy
Accepted
9 minutes |2 попытки
"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            if len(set(s)) < len(goal):
                return True
            else:
                return False
        else:
            if len(s) != len(goal):
                return False
            else:
                count_diff = 0
                for i in range(len(s)):
                    if s[i] != goal[i]:
                        count_diff += 1
                if count_diff == 2:
                    x = list(s)
                    x.sort()
                    y = list(goal)
                    y.sort()
                    if x == y:
                        return True
                    else:
                        return False
                else:
                    return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.buddyStrings('ab', 'ba') == True
    assert solution.buddyStrings('ab', 'ab') == False
    assert solution.buddyStrings('aa', 'aa') == True
    assert solution.buddyStrings('abcaa', 'abcbb') == False
