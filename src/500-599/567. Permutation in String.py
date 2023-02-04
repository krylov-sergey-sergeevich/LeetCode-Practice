from src.AssertUtils import check

"""
https://leetcode.com/problems/permutation-in-string/

567. Permutation in String
567. Перестановка в строке
Medium
Accepted
"""


def str_to_dict_count(s: str) -> dict[str, int]:
    """
    Подсчет символов в строке и возвращение соотношения <символ, число>.

    :param s: строка
    :return: словарь
    """
    d = dict()
    for el in s:
        if el not in d:
            d[el] = 1
        else:
            d[el] = d[el] + 1
    return d


def check_equals_dict_key_value(d1: dict[str, int], d2: dict[str, int]) -> bool:
    if len(d1) != len(d2):
        return False
    for k in d1.keys():
        if k not in d2:
            return False
        if d1[k] != d2[k]:
            return False
    return True


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        blocks = []
        d = str_to_dict_count(s1)
        pred = 0
        for idx in range(len(s2)):
            if s2[idx] not in d:
                blocks.append(s2[pred:idx])
                pred = idx + 1
            else:
                if idx == len(s2) - 1:
                    blocks.append(s2[pred:])
        # print(blocks)
        blocks = list(filter(lambda it: len(it) >= l1, blocks))
        if len(blocks) == 0:
            return False
        # print(blocks)
        for block in blocks:
            block_d = str_to_dict_count(block[:l1])
            res = check_equals_dict_key_value(d, block_d)
            if res:
                return True
            for idx in range(l1, len(block)):
                if block[idx] not in block_d:
                    block_d[block[idx]] = 1
                else:
                    block_d[block[idx]] = block_d[block[idx]] + 1
                block_d[block[idx - l1]] = block_d[block[idx - l1]] - 1
                res = check_equals_dict_key_value(d, block_d)
                if res:
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()

    check(solution.checkInclusion("ab", "eidbaooo"), True)
    check(solution.checkInclusion("ab", "eidboaoo"), False)
    check(solution.checkInclusion("abc", "abc"), True)
    check(solution.checkInclusion("abc", "acb"), True)
    check(solution.checkInclusion("abc", "bca"), True)
    check(solution.checkInclusion("aaa", "abc"), False)
    check(solution.checkInclusion("adc", "dcda"), True)
    check(solution.checkInclusion("bb", "aabbcc"), True)
    check(solution.checkInclusion("bdb", "aabdbbdcc"), True)
    check(solution.checkInclusion("a", "ab"), True)
