import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import algo_dijkstra

class DijkstraVisualizer:
    def __init__(self, graph):
        self.graph = graph
        self.pos = nx.spring_layout(graph)
        self.result_file = open('result_dijkstra.txt', 'r')
        self.lines = self.result_file.readlines()
        self.current_line_index = 0
        self.distance_labels = {}
        self.used_edges = []

        self.fig, self.ax = plt.subplots()
        self.text_plot = plt.subplot()
        self.plot_graph()

        ax_next = plt.axes([0.7, 0.05, 0.2, 0.075])
        self.next_button = Button(ax_next, 'Следующий шаг')
        self.next_button.on_clicked(self.next_step)

        self.distance_labels[1] = 0

        plt.show()

    def plot_graph(self):
        self.ax.clear()
        nx.draw_networkx_nodes(self.graph, self.pos, node_color='lightblue', ax=self.ax)
        nx.draw_networkx_labels(self.graph, self.pos, ax=self.ax)
        nx.draw_networkx_edges(self.graph, self.pos, width=2, edge_color='gray', ax=self.ax)

        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=labels, ax=self.ax)

        for (start_node, end_node) in self.used_edges:
            nx.draw_networkx_edges(self.graph, self.pos, edgelist=[(start_node, end_node)],
                                   width=2, edge_color='red', ax=self.ax)

        for node in self.graph.nodes:
            if (node in self.distance_labels):
                self.text_plot.text(self.pos[node][0] + 0.05, self.pos[node][1] + 0.05, f"{self.distance_labels[node]}", ha='center',
                                    va='bottom')

        self.ax.set_title("Алгоритм Дейкстры")
        self.ax.axis('off')

    def next_step(self, event):
        if self.current_line_index >= len(self.lines):
            return

        line = self.lines[self.current_line_index].strip()
        start_node, end_node, distance = map(int, line.split(' '))
        print(start_node, end_node, distance)


        if (end_node != -1):
            self.used_edges.append((start_node, end_node))
            self.distance_labels[end_node] = distance

            self.graph.nodes[end_node]['label'] = distance

        self.plot_graph()

        nx.draw_networkx_nodes(self.graph, self.pos, nodelist=[start_node],
                               node_color='green', ax=self.ax)

        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=labels, ax=self.ax)

        self.fig.canvas.draw_idle()

        self.current_line_index += 1


def start(G):
    with open('graph.txt', 'w') as f:
        f.write(f"{G.number_of_nodes()} {G.number_of_edges()}\n")
        for u, v, weight in G.edges(data=True):
            f.write(f"{u} {v} {weight['weight']}\n")

    algo_dijkstra.main()

    visualizer = DijkstraVisualizer(G)
    plt.ioff()

# Использование
if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge(1, 2, weight=1)
    G.add_edge(2, 3, weight=12)
    G.add_edge(1, 4, weight=5)
    G.add_edge(4, 5, weight=2)
    G.add_edge(5, 3, weight=1)
    G.add_edge(3, 6, weight=7)
    G.add_edge(6, 8, weight=10)
    G.add_edge(6, 7, weight=4)
    G.add_edge(8, 9, weight=2)
    G.add_edge(7, 9, weight=2)
    start(G)