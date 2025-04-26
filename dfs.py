def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            neighbors = graph[node] if node in graph else []
            stack.extend(neighbors)

    return visited

graph = {1: [3], 2: [4], 4: [2]}

start_node = 1
path = dfs(graph, start_node)
print(f"DFS path from node {start_node}: {path}") 

