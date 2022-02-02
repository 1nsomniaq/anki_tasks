graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


visited = set()


def dfs(visited, graph, root):  # function for dfs
    if root not in visited:
        print(root)
        visited.add(root)
        for n in graph[root]:
            if n not in visited:
                dfs(visited, graph, n)




# start with '5'
dfs(visited, graph, '5')
