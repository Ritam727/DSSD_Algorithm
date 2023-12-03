import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, n, p, s, src):
        self.n = n
        self.adj = np.zeros((n, n))
        self.val = np.zeros(n)
        self.rem = np.zeros(n)
        self.e1 = np.zeros(n)
        self.color_map = np.array(["cyan" for i in range(self.n)]).astype("object")
        self.color_map[src] = "green"
        self.src = src
        self.e1[src] = 1
        self.p = p
        self.s = s
        
    def add_edge(self, u, v):
        self.adj[u][v] = 1
        self.adj[v][u] = 1
        
    def drop_edges(self):
        prod = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(i, self.n):
                if self.adj[i][j] == 1:
                    prod[i][j] = np.random.choice([0, 1], p = [self.p, 1 - self.p])
                    prod[j][i] = prod[i][j]
        if np.sum(prod) < np.sum(self.adj):
            print((np.sum(self.adj) - np.sum(prod)) // 2, "links failed")
        self.adj = np.multiply(self.adj, prod)

    def drop_nodes(self):
        cnt = 0
        for i in range(self.n):
            val = np.random.choice([1, 0], p = [self.p / self.n, 1 - self.p / self.n])
            if val == 1 and self.rem[i] == 0 and i != self.src:
                for j in range(self.n):
                    self.adj[i][j] = 0
                    self.adj[j][i] = 0
                self.rem[i] = 1
                cnt += 1
        if cnt > 0:
            print(cnt, "nodes failed")

    def introduce_failure(self):
        self.drop_nodes()
        self.drop_edges()

    def save_init_graph(self, name):
        drawing = nx.from_numpy_array(self.adj)
        nx.draw(drawing, node_color = self.color_map, with_labels = True)
        plt.savefig("images/" + name + ".png")
        plt.close()

    def draw_graph(self, name):
        self.color_map[np.where(self.rem == 1)] = "gray"
        self.color_map[np.where(self.val < 1e-4)] = "gray"
        self.color_map[np.where(self.rem == 1)] = "red"
        drawing = nx.from_numpy_array(self.adj)
        nx.draw(drawing, node_color = self.color_map, with_labels = True)
        plt.savefig("images/" + name + ".png")
        plt.close()
    
    def update_values(self):
        D = np.zeros((self.n, self.n))
        I = np.zeros((self.n, self.n))
        for i in range(self.n):
            D[i][i] = np.sum(self.adj[i])
            I[i][i] = 1
        self.val = np.dot(np.linalg.inv(D + I), (np.dot(self.adj, self.val) + self.s * self.e1))
        self.val[np.where(self.rem == 1)] = -1