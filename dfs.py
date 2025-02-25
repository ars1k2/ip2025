import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import algo_dfs

class dfsVisualizer:
    def __init__(self, graph):
        self.graph = graph
        self.pos = nx.spring_layout(graph)
        self.result_file = open('result_dfs.txt', 'r')
        self.lines = self.result_file.readlines()
        self.current_line_index = 0
        self.used_edges = []

        self.fig, self.ax = plt.subplots()
        self.text_plot = plt.subplot()
        self.plot_graph()

        ax_next = plt.axes([0.7, 0.05, 0.2, 0.075])
        self.next_button = Button(ax_next, 'Следующий шаг')
        self.next_button.on_clicked(self.next_step)

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

        self.ax.set_title("Обхрд в глубину")
        self.ax.axis('off')

    def next_step(self, event):
        if self.current_line_index >= len(self.lines):
            return

        line = self.lines[self.current_line_index].strip()
        start_node, end_node = map(int, line.split(' '))

        if (end_node != -1):
            self.used_edges.append((start_node, end_node))

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
            f.write(f"{u} {v}\n")

    algo_dfs.main()

    visualizer = dfsVisualizer(G)
    plt.ioff()
