import heapq
import sys


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    n, m = map(int, lines[0].split())

    max_vertex = n
    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        max_vertex = max(max_vertex, u)

    graph = [[] for _ in range(max_vertex)]

    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    return n, graph

p = ""
used = []
s = set()
def dfs_dfs(graph, v):
    global p, used, s
    used[v] = 1;
    p += f"{v + 1} {-1}\n"

    for i in graph[v]:
        if ((i, v) in s):
            continue
        p += f"{v + 1} {i + 1}\n"
        s.add((v, i))
        if used[i] == 0:
            dfs_dfs(graph, i)


def dfs(n, graph):
    global p, used
    used = [0] * n
    p = ""
    dfs_dfs(graph, 0)
    print(p)
    with open("result_dfs.txt", 'w') as file:
        file.write(p)

def main():
    n, graph = read_graph_from_file('graph.txt')
    dfs(n, graph)

if __name__ == "__main__":
    main()