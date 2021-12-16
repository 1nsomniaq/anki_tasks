class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            return [x for x in range(n)]

        tree = [set() for _ in range(n)]

        for start, end in edges:
            tree[start].add(end)
            tree[end].add(start)

        leaves = []

        for node_index in range(n):
            if len(tree[node_index]) == 1:
                leaves.append(node_index)

        unprocessed_count = n

        while unprocessed_count > 2:
            unprocessed_count -= len(leaves)

            new_leaves = []

            while leaves:
                leaf_index = leaves.pop()
                neighbour = tree[leaf_index].pop()
                tree[neighbour].remove(leaf_index)

                if len(tree[neighbour]) == 1:
                    new_leaves.append(neighbour)

            leaves = new_leaves

        return leaves