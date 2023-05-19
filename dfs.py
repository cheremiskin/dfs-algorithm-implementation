import sys


# Function for creating an adjacency matrix
def create_adjacency_matrix(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v)
        graph[v].add(u)
    return graph


# Depth-first search function
def dfs(graph, start, end):
    visited = set()
    stack = [(start, 0)]
    path_length = -1

    while stack:
        vertex, count = stack.pop()

        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            if vertex == end:
                path_length = count
            for neighbor in graph[vertex]:
                stack.append((neighbor, count + 1))

    return path_length


if __name__ == "__main__":
    filename = sys.argv[1]
    start_vertex = int(sys.argv[2])
    end_vertex = int(sys.argv[3])
    edges = []
    with open(filename, "r") as file:
        for line in file:
            u, v = map(int, line.strip().split())
            edges.append((int(u), int(v)))
    graph = create_adjacency_matrix(edges)

    if start_vertex not in graph or end_vertex not in graph:
        raise Exception("Одна или обе вершины отсутствуют в ребрах.")

    path_length = dfs(graph, start_vertex, end_vertex)
    print(f'Длина пути: {path_length}')
