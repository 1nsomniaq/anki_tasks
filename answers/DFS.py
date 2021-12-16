graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()


def dfs(graph, root, visited):  # function for dfs
  if root not in visited:
    print(root)
    visited.add(root)
    for neighbour_index in graph[root]:
            dfs(graph, neighbour_index, visited)


# start with '5'
dfs(graph, '5', visited)
