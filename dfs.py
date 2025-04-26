def dfs_path_length(graph, start_node, end_node):
    # Checking the starting and ending vertices in the graph
    if start_node not in graph or end_node not in graph:
        print("Error: Invalid start or end node")
        return -1

    visited = set()# Посещенные вершины
    stack = [(start_node, 0)]  

    while stack:
        node, path_length = stack.pop()
        if node == end_node:
            return path_length  # The path has been found
        if node not in visited:
            visited.add(node)
            neighbors = graph[node] if node in graph else []
            for neighbor in neighbors:
                stack.append((neighbor, path_length + 1))
    return -1  # Путь не найден

# Пример
graph = {1: [3], 2: [4], 4: [2]}

# Начальная и конечная точка
start_node = 2
end_node = 4

# Ответ
path_length = dfs_path_length(graph, start_node, end_node)
print(f"Path length from {start_node} to {end_node}: {path_length}")  

