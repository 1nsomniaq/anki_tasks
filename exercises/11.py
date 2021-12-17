class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        null_pointer = None
        pointer = None

        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                if null_pointer is None:
                    null_pointer = i
                    break

        if null_pointer is None:
            return

        while null_pointer < n:

            pointer = null_pointer

            while nums[pointer] == 0:
                pointer += 1
                if pointer >= n:
                    return

            nums[pointer], nums[null_pointer] = nums[null_pointer], nums[pointer]

            null_pointer = pointer

            while nums[null_pointer] != 0:
                null_pointer += 1


Solution().moveZeroes([0, 1, 0, 3, 12])