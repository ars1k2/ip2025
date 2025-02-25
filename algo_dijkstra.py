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

    for i in range(1, m + 1):
        u, v, w = map(int, lines[i].split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    return n, graph


def dijkstra(n, graph):
    distances = [float('inf')] * n
    used = [0] * n
    distances[0] = 0

    with open("result_dijkstra.txt", 'w') as file:
        for p in range(n):
            cur = 0
            cur_dist = float('inf')
            for i in range(n):
                if (distances[i] < cur_dist and used[i] == 0):
                    cur_dist = distances[i]
                    cur = i

            c = 0
            for u, w in graph[cur]:
                if (distances[u] > cur_dist + w and used[u] == 0):
                    file.write(f"{cur + 1} {u + 1} {cur_dist + w}\n")
                    c+=1
                    distances[u] = cur_dist + w
                elif (used[u] == 0):
                    c += 1
                    file.write(f"{cur + 1} {u + 1} {distances[u]}\n")

            used[cur] = 1
            if (c == 0):
                file.write(f"{cur + 1} {-1} {cur_dist + w}\n")


def main():
    n, graph = read_graph_from_file('graph.txt')
    dijkstra(n, graph)

if __name__ == "__main__":
    main()