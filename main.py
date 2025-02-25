import tkinter as tk
from tkinter import scrolledtext
import networkx as nx
from tkinter import messagebox
import dijkstra
import kruskal
import dfs

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.dijkstra = tk.Button(self)
        self.dijkstra["text"] = "Алгоритм Дейкстры"
        self.dijkstra["command"] = self.open_input_menu_dijkstra
        self.dijkstra["width"] = 40
        self.dijkstra["height"] = 5
        self.dijkstra["font"] = ("Arial", 14)
        self.dijkstra.pack(side="top")
        self.kruskal = tk.Button(self)
        self.kruskal["text"] = "Алгоритм Краскалла"
        self.kruskal["command"] = self.open_input_menu_kruskal
        self.kruskal["width"] = 40
        self.kruskal["height"] = 5
        self.kruskal["font"] = ("Arial", 14)
        self.kruskal.pack(side="top")
        self.dfs = tk.Button(self)
        self.dfs["text"] = "Обход в глубину"
        self.dfs["command"] = self.open_input_menu_dfs
        self.dfs["width"] = 40
        self.dfs["height"] = 5
        self.dfs["font"] = ("Arial", 14)
        self.dfs.pack(side="top")

    def open_input_menu_dijkstra(self):
        input_window = tk.Toplevel(self.master)
        input_window.title("Ввод графа")

        label = tk.Label(input_window, text="Введите граф в формате вершина вершина вес:")
        label["width"] = 40
        label["height"] = 5
        label["font"] = ("Arial", 14)
        label.pack()

        text_area = scrolledtext.ScrolledText(input_window, width=50, height=10)
        text_area.pack(pady=10)
        text_area["font"] = ("Arial", 14)

        def submit_input_dijkstra():
            G = nx.Graph()
            graph_input = text_area.get("1.0", tk.END).strip().split('\n')
            graph = []
            for line in graph_input:
                parts = line.strip().split()
                if len(parts) == 3:
                    try:
                        vertex1 = int(parts[0])
                        vertex2 = int(parts[1])
                        weight = int(parts[2])
                        G.add_edge(vertex1, vertex2, weight=weight)
                        graph.append((vertex1, vertex2, weight))
                    except ValueError:
                        messagebox.showerror("Ошибка", "Неправильный формат ввода. Все значения должны быть числами.")
                        return

            if not graph:
                messagebox.showerror("Ошибка", "Граф не может быть пустым.")
                return

            input_window.destroy()

            dijkstra.start(G)

        submit_button = tk.Button(input_window, text="Готово", command=submit_input_dijkstra)
        submit_button["width"] = 30
        submit_button["height"] = 5
        submit_button["font"] = ("Arial", 14)
        submit_button.pack()

    def open_input_menu_kruskal(self):
        input_window = tk.Toplevel(self.master)
        input_window.title("Ввод графа")

        label = tk.Label(input_window, text="Введите граф в формате вершина вершина вес:")
        label["width"] = 40
        label["height"] = 5
        label["font"] = ("Arial", 14)
        label.pack()

        text_area = scrolledtext.ScrolledText(input_window, width=50, height=10)
        text_area.pack(pady=10)
        text_area["font"] = ("Arial", 14)

        def submit_input_kruskal():
            G = nx.Graph()
            graph_input = text_area.get("1.0", tk.END).strip().split('\n')
            graph = []
            for line in graph_input:
                parts = line.strip().split()
                if len(parts) == 3:
                    try:
                        vertex1 = int(parts[0])
                        vertex2 = int(parts[1])
                        weight = int(parts[2])
                        G.add_edge(vertex1, vertex2, weight=weight)
                        graph.append((vertex1, vertex2, weight))
                    except ValueError:
                        messagebox.showerror("Ошибка",
                                             "Неправильный формат ввода. Все значения должны быть числами.")
                        return
                else:
                    messagebox.showerror("Ошибка",
                                         "Неправильный формат ввода. Все значения должны быть числами.")
                    return

            if not graph:
                messagebox.showerror("Ошибка", "Граф не может быть пустым.")
                return

            kruskal.start(G)
            input_window.destroy()


        submit_button = tk.Button(input_window, text="Готово", command=submit_input_kruskal)
        submit_button["width"] = 30
        submit_button["height"] = 5
        submit_button["font"] = ("Arial", 14)
        submit_button.pack()

    def open_input_menu_dfs(self):
        input_window = tk.Toplevel(self.master)
        input_window.title("Ввод графа")

        label = tk.Label(input_window, text="Введите граф в формате вершина вершина:")
        label["width"] = 40
        label["height"] = 5
        label["font"] = ("Arial", 14)
        label.pack()

        text_area = scrolledtext.ScrolledText(input_window, width=50, height=10)
        text_area.pack(pady=10)
        text_area["font"] = ("Arial", 14)

        def submit_input_dfs():
            G = nx.Graph()
            graph_input = text_area.get("1.0", tk.END).strip().split('\n')
            graph = []
            for line in graph_input:
                parts = line.strip().split()
                if len(parts) == 2:
                    try:
                        vertex1 = int(parts[0])
                        vertex2 = int(parts[1])
                        G.add_edge(vertex1, vertex2)
                        graph.append((vertex1, vertex2))
                    except ValueError:
                        messagebox.showerror("Ошибка", "Неправильный формат ввода. Все значения должны быть числами.")
                        return

            if not graph:
                messagebox.showerror("Ошибка", "Граф не может быть пустым.")
                return

            input_window.destroy()

            dfs.start(G)

        submit_button = tk.Button(input_window, text="Готово", command=submit_input_dfs)
        submit_button["width"] = 30
        submit_button["height"] = 5
        submit_button["font"] = ("Arial", 14)
        submit_button.pack()

root = tk.Tk()
root.title("Выбор алгоритма")
app = Application(master=root)
app.mainloop()
