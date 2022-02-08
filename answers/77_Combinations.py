"""Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 1, 2, 3, 4 k=3


        # backtrack

        res = []

        def backtrack(start, s):
            if len(s) == k:
                res.append(s[:])

            for i in range(start, n+1):   # от 1 до 5 вкл
                s.append(i)               # s = [1]
                backtrack(i + 1, s)       # bt [2, 5]
                s.pop()

        backtrack(1, [])

        return res
