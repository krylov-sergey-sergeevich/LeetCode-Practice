# https://leetcode.com/problems/student-attendance-record-ii/
# Hard
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        # кэш для хранения результатов
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        # Функция считает приемлемые комбинации
        # total_absences - число отсутствий
        # consecutive_lates - кол-во опозданий последовательных
        def eligible_combinations(n, total_absences, consecutive_lates):
            if total_absences >= 2 or consecutive_lates >= 3:
                return 0
            if n == 0:
                return 1
            if memo[n][total_absences][consecutive_lates] != -1:
                return memo[n][total_absences][consecutive_lates]

            # Выбираем 'P' для текущей позиции
            count = eligible_combinations(n - 1, total_absences, 0)
            # Выбираем 'A' для текущей позиции
            count = (
                            count +
                            eligible_combinations(n - 1, total_absences + 1, 0)
                    ) % MOD
            # Выбираем 'L' для текущей позиции
            count = (
                            count +
                            eligible_combinations(n - 1,
                                                  total_absences,
                                                  consecutive_lates + 1)
                    ) % MOD

            # Сохраняем результат в кэш
            memo[n][total_absences][consecutive_lates] = count
            return count

        return eligible_combinations(n, 0, 0)

    def checkRecord2(self, n: int) -> int:
        MOD = 1000000007
        # Cache to store sub-problem results.
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        # Base case: there is 1 string of length 0 with zero 'A' and zero 'L'.
        dp[0][0][0] = 1

        # Iterate on smaller sub-problems and use the current smaller sub-problem
        # to generate results for bigger sub-problems.
        for length in range(n):
            for total_absences in range(2):
                for consecutive_lates in range(3):
                    # Store the count when 'P' is chosen.
                    dp[length + 1][total_absences][0] = (
                                                                dp[length + 1][total_absences][0] +
                                                                dp[length][total_absences][consecutive_lates]
                                                        ) % MOD
                    # Store the count when 'A' is chosen.
                    if total_absences < 1:
                        dp[length + 1][total_absences + 1][0] = (
                                                                        dp[length + 1][total_absences + 1][0] +
                                                                        dp[length][total_absences][consecutive_lates]
                                                                ) % MOD
                    # Store the count when 'L' is chosen.
                    if consecutive_lates < 2:
                        dp[length + 1][total_absences][consecutive_lates + 1] = (
                                                                                        dp[length + 1][total_absences][
                                                                                            consecutive_lates + 1] +
                                                                                        dp[length][total_absences][
                                                                                            consecutive_lates]
                                                                                ) % MOD

        # Sum up the counts for all combinations of length 'n' with different absent and late counts.
        count = 0
        for total_absences in range(2):
            for consecutive_lates in range(3):
                count = (count +
                         dp[n][total_absences][consecutive_lates]) % MOD

        return count


if __name__ == '__main__':
    solution = Solution()
    assert solution.checkRecord(2) == 8
    assert solution.checkRecord2(10101) == 183236316
