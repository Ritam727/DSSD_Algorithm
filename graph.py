import numpy as np

class Graph:
    def __init__(self, n, p, s):
        self.n = n
        self.adj = np.zeros((n, n))
        self.val = np.zeros(n)
        self.e1 = np.zeros(n)
        self.e1[0] = 1
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
            print("cut introduced")
        self.adj = np.multiply(self.adj, prod)
        
    def update_values(self):
        D = np.zeros((self.n, self.n))
        I = np.zeros((self.n, self.n))
        for i in range(self.n):
            D[i][i] = np.sum(self.adj[i])
            I[i][i] = 1
        self.val = np.dot(np.linalg.inv(D + I), (np.dot(self.adj, self.val) + self.s * self.e1))