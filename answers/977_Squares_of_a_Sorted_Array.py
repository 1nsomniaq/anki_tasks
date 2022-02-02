'''
Given an integer array nums sorted in non-decreasing order,
 return an array of the squares of each number sorted in non-decreasing order.
'''


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        left = 0
        right = len(nums) - 1

        while left < right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] * nums[left])
                left += 1
            else:
                res.append(nums[right] * nums[right])
                right -= 1

        return res