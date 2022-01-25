class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        dist = [[-1] * len(mat[0]) for _ in range(len(mat))]

        queue = []

        def is_valid(r, c, r_max, c_max):
            if r < 0 or r > r_max or c < 0 or c > c_max:
                return False
            return True

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r == 0 and c == 1:
                    pass
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        ns = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            curr_r, curr_c = queue.pop(0)

            for add_r, add_c in ns:
                n_r, n_c = curr_r + add_r, curr_c + add_c

                if is_valid(n_r, n_c, len(mat) - 1, len(mat[0]) - 1) and dist[n_r][n_c] == -1:
                    dist[n_r][n_c] = dist[curr_r][curr_c] + 1
                    queue.append((n_r, n_c))

        return dist


sol = Solution()

print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
