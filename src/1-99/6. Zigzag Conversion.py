from src.AssertUtils import check

"""
https://leetcode.com/problems/zigzag-conversion/

6. Zigzag Conversion
Medium
Accepted
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        j = 0
        down = True
        diag = False
        data = ["" for i in range(numRows)]
        for el in s:
            # print("---")
            # print(f"i={i}, j={j} el={el} | down={down}, diag={diag}")
            data[i] = data[i] + el
            if down and i == numRows - 1 and i == 0:
                # print("0")
                pass
            elif down and i < numRows - 1:
                # print("1")
                i += 1
                if i == numRows:
                    down = False
                    diag = True
            elif down and i == numRows - 1:
                # print("2")
                down = False
                diag = True
                i -= 1
                j += 1
                if i == 0:
                    down = False
                    diag = True
            elif diag and i == 0:
                # print("3")
                down = True
                diag = False
                i += 1
                if i == numRows:
                    down = True
                    diag = False
            elif diag and i != 0:
                # print("4")
                i -= 1
                j += 1
                if i == 0:
                    down = True
                    diag = False
            else:
                raise Exception(f"Непредвиденная ситуация down={down}, diag={diag} => i = {i}, j = {j}")
            # print(f"i={i}, j={j} el={el} | down={down}, diag={diag}")
        return "".join(data)


class BestSolution():
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = ['' for _ in range(numRows)]
        row = 0
        step = 1
        for c in s:
            zigzag[row] += c
            if row == numRows - 1:
                step = -1
            elif row == 0:
                step = 1
            row += step
        return ''.join(zigzag)


if __name__ == "__main__":
    solution = Solution()
    print("=== Run solution ===")

    check(solution.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
    check(solution.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
    check(solution.convert("A", 1), "A")
    check(solution.convert("ABC", 2), "ACB")
    check(solution.convert("ABC", 1), "ABC")

    solution = BestSolution()
    print("=== Run best solution ===")
    check(solution.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
    check(solution.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
    check(solution.convert("A", 1), "A")
    check(solution.convert("ABC", 2), "ACB")
    check(solution.convert("ABC", 1), "ABC")

"""
P     I    N
A   L S  I G
Y A   H R
P     I
"""

"""
P  A  H
A PL SI
Y  I
     
"""
