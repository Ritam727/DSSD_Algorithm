from graph import Graph
import numpy as np
import argparse

parser = argparse.ArgumentParser(prog = "main.py", description = "Simulate DSSD Algorithm")
parser.add_argument("filename", type = str, help = "Name of file from which to read graph description")

args = parser.parse_args()

try:
    f = open(args.filename, "r")
    lines = f.readlines()
    n, m = 0, 0
    n, m, src, p, s = map(float, lines[0].split())
    n, m, s, src = map(int, [n, m, s, src])
    gr = Graph(n, p, s, src)
    for i in range(m):
        u, v = map(int, lines[i + 1].split())
        gr.add_edge(u, v)
    gr.save_init_graph()
    for i in range(500):
        gr.introduce_failure()
        gr.update_values()
        if i % 100 == 99:
            gr.draw_graph(i)
            print(i + 1, "simulations complete")
            for j in gr.val:
                print("%.4f"%(j), end = " ")
            print()
except FileNotFoundError:
    print("Please provide valid file")