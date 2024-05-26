from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result: list[str] = []

        def dfs(s: str, draftResult: str):
            if len(s) == 0:
                result.append(draftResult)
            for word in wordDict:
                if s.startswith(word):
                    if len(draftResult) == 0:
                        new_draft = word
                    else:
                        new_draft = draftResult + " " + word
                    dfs(s[len(word):], new_draft)

        dfs(s, "")
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    assert solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == ["cats and dog", "cat sand dog"]
