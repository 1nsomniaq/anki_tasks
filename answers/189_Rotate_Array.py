'''Given an array, rotate the array to the right by k steps, where k is non-negative.'''


# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        while k >= len(nums):
            k = k % len(nums)

        if k == 0:
            return

        def swap(left_i, right_i):
            while left_i < right_i:
                nums[left_i], nums[right_i] = nums[right_i], nums[left_i]
                left_i += 1
                right_i -= 1

        swap(0, len(nums)-1)
        swap(0, k-1)
        swap(k, len(nums)-1)

