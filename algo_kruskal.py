import heapq
import sys


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    n, m = map(int, lines[0].split())

    max_vertex = n
    for i in range(1, m + 1):
        u, v, w = map(int, lines[i].split())
        max_vertex = max(max_vertex, u, v)

    graph = [[] for _ in range(max_vertex)]
    edges = []

    for i in range(1, m + 1):
        u, v, w = map(int, lines[i].split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))

    return n, graph, edges


def kruskal(n, graph, edges):
    comp = [0] * n
    used = [0] * len(edges)
    for i in range(n):
        comp[i] = i

    with open("result_kruskal.txt", 'w') as file:
        while True:
            min_ind = -1
            for i in range(len(edges)):
                if (used[i] == 0 and (edges[i][2] < edges[min_ind][2] or min_ind == -1)):
                    min_ind = i

            if (min_ind == -1):
                break

            used[min_ind] = 1
            u = edges[min_ind][0]
            v = edges[min_ind][1]

            if (comp[u] == comp[v]):
                file.write(f"{u + 1} {v + 1} {2}\n")
                continue

            file.write(f"{u + 1} {v + 1} {1}\n")
            for i in range(n):
                if (comp[i] == comp[u]):
                    comp[i] = comp[v]



def main():
    n, graph, edges = read_graph_from_file('graph.txt')
    kruskal(n, graph, edges)

if __name__ == "__main__":
    main()