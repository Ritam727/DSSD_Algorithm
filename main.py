from graph import Graph
import numpy as np

graph_ = Graph(5, 0.01, 10)

graph_.add_edge(0, 1)
graph_.add_edge(1, 2)
graph_.add_edge(2, 3)
graph_.add_edge(3, 4)
graph_.add_edge(0, 4)

cnts = np.zeros(5)

for i in range(100):
    if i > 60:
        graph_.adj[1][2] = graph_.adj[2][1] = 0
        graph_.adj[3][4] = graph_.adj[4][3] = 0
    graph_.update_values()
    print(graph_.val)
    for i in range(5):
        if graph_.val[i] < 1e-5:
            if cnts[i] > 5:
                print("Node " + str(i) + " is disconnected from source")
            cnts[i] += 1
        else:
            cnts[i] = 0

print(graph_.val)