class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return

        nums.sort()

        res = []
        for i in range(len(nums)-2):
            if i > 0:
                break

            j = i + 1
            k = len(nums) - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    res.append((nums[i], nums[j], nums[k]))
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1

        return res


