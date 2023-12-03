from graph import Graph
import argparse
import numpy as np
import matplotlib.pyplot as plt
import random
import os

parser = argparse.ArgumentParser(prog = "main.py", description = "Simulate DSSD Algorithm")
parser.add_argument("filename", type = str, help = "Name of file from which to read graph description")
parser.add_argument("graphtype", type = str, help = "Type of graph, will be used as prefix for naming graph drawings")

args = parser.parse_args()

if "images" not in os.listdir():
    os.mkdir("images")

try:
    f = open(args.filename, "r")
    graph_name = args.graphtype
    lines = f.readlines()
    n, m = 0, 0
    n, m, src, p, s, sims = map(float, lines[0].split())
    n, m, s, src, sims = map(int, [n, m, s, src, sims])
    gr = Graph(n, p, s, src)
    for i in range(m):
        u, v = map(int, lines[i + 1].split())
        gr.add_edge(u, v)
    gr.save_init_graph(graph_name)
    value_matrix = [gr.val]
    elements = [0, int(n / 3), int(2 * n / 3), n - 1]
    for i in range(sims):
        if i < 200:
            gr.introduce_failure()
        gr.update_values()
        value_matrix.append(gr.val)
        if i % 100 == 99:
            gr.draw_graph(graph_name + str(i))
            print(i + 1, "simulations complete")
            for j in gr.val:
                print("%.4f"%(j), end = " ")
            print()
    value_matrix = np.array(value_matrix)
    x_ = list(range(1001))
    fig, ax = plt.subplots(2, 2, figsize = (10, 10))
    fig.suptitle("Values at few nodes in the network")
    fig.supxlabel("Iterations")
    fig.supylabel("Value at node")
    ax[0][0].set_title("value at node " + str(elements[0]))
    ax[0][0].plot(x_, value_matrix[:, elements[0]])
    ax[0][1].set_title("value at node " + str(elements[1]))
    ax[0][1].plot(x_, value_matrix[:, elements[1]])
    ax[1][0].set_title("value at node " + str(elements[2]))
    ax[1][0].plot(x_, value_matrix[:, elements[2]])
    ax[1][1].set_title("value at node " + str(elements[3]))
    ax[1][1].plot(x_, value_matrix[:, elements[3]])
    fig.subplots_adjust(hspace = 0.4)
    plt.savefig("fig.png")
except FileNotFoundError:
    print("Please provide valid file")