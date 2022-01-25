graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


visited = set()
stack = []

def dfs(visited, graph, root):  # function for dfs
    stack.append(root)

    while stack:
        curr = stack.pop()
        print(curr)
        if curr not in visited:
            visited.add(curr)
            for n in graph[curr]:
                if n not in visited:
                    stack.append(n)





# start with '5'
dfs(visited, graph, '5')
