class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res

if __name__ == '__main__':
    solution = Solution()

    print(solution.shuffle([2, 5, 1, 3, 4, 7], 3))
    print(solution.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
