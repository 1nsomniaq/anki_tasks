from functools import reduce

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        r_res = []
        left_window = 1
        right_window = reduce(lambda x, y: x * y, nums[1:])
        res.append(left_window)
        r_res.append(right_window)

        for i in range(1, len(nums)):
            left_window *= nums[i-1]
            right_window /= nums[i]
            res.append(left_window)
            r_res.append(right_window)

        return res


print(Solution().productExceptSelf([1, 2, 3, 4]))
