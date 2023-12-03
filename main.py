from graph import Graph
import argparse
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
    for i in range(sims):
        gr.introduce_failure()
        gr.update_values()
        if i % 100 == 99:
            gr.draw_graph(graph_name + str(i))
            print(i + 1, "simulations complete")
            for j in gr.val:
                print("%.4f"%(j), end = " ")
            print()
except FileNotFoundError:
    print("Please provide valid file")