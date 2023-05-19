import sys


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)


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


if __name__ == "__main__":
    filename = sys.argv[1]
    start_vertex = int(sys.argv[2])
    edges = []
    with open(filename, "r") as file:
        for line in file:
            u, v = map(int, line.strip().split())
            edges.append((int(u), int(v)))
    graph = create_adjacency_matrix(edges)
    dfs(graph, start_vertex)
