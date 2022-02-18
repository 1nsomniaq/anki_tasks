class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l = 0
        r = len(arr) - 1

        if len(arr) <= k:
            return arr

        while l + 1 < r:
            p = l + (r - l) // 2

            if arr[p] >= x and abs(arr[p] - x) < abs(arr[r] - x):
                r = p
            else:
                l = p

        closest = l if x - arr[l] <= arr[r] - x else r
        # left = bisect_left(arr, x)

        s = e = closest
        res = [arr[closest]]

        while e - s + 1 < k:

            if s == -1:
                e += 1
                continue

            if e >= len(arr) - 1 or (s > 0 and x - arr[s - 1] <= arr[e + 1] - x):
                s -= 1
            else:
                e += 1

        return arr[s:e + 1]


Solution().findClosestElements(
    [1, 1, 2, 2, 3, 3, 6, 7, 8, 9, 9, 11, 11, 12, 12, 12, 13, 15, 18, 18, 21, 22, 22, 23, 25],
    # , 25, 32, 33, 34, 37, 37, 38,
    # 38, 39, 39, 40, 41, 43, 43, 45, 45, 46, 46, 48, 48, 49, 50, 50, 53, 53, 54, 54, 56, 57, 57, 58, 58, 60, 60, 61, 62, 63,
    # 63, 66, 69, 70, 71, 71, 71, 74, 75, 75, 76, 76, 80, 81, 81, 82, 84, 86, 86, 87, 87, 87, 88, 90, 91, 93, 93, 93, 94, 94,
    # 94, 95, 96, 97, 98, 98, 98, 99],
    3,
    13)
