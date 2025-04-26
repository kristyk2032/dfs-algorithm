def dfs_path_length(graph, start_node, end_node):
    if start_node not in graph or end_node not in graph:
        print("Error: Invalid start or end node")
        return -1

    visited = set()
    stack = [(start_node, 0)]  

    while stack:
        node, path_length = stack.pop()
        if node == end_node:
            return path_length  
        if node not in visited:
            visited.add(node)
            neighbors = graph[node] if node in graph else []
            for neighbor in neighbors:
                stack.append((neighbor, path_length + 1))

    return -1  

graph = {1: [3], 2: [4], 4: [2]}

start_node = 2
end_node = 4

path_length = dfs_path_length(graph, start_node, end_node)
print(f"Path length from {start_node} to {end_node}: {path_length}")  

