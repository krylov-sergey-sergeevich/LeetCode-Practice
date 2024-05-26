# https://leetcode.com/problems/reverse-prefix-of-word
# Easy
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        else:
            return word[:idx + 1][::-1] + word[idx + 1:]


if __name__ == '__main__':
    solution = Solution()
    assert solution.reversePrefix("abcdefd", "d") == "dcbaefd"
    assert solution.reversePrefix("xyxzxe", "z") == "zxyxxe"
    assert solution.reversePrefix("abcd", "z") == "abcd"
