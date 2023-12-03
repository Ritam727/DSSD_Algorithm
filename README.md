# DSSD Algorithm

## Requirements
Before running the simulations, we are required to install the dependencies which are mentioned in the `requirements.txt` file. These can be installed with the following command:
```bash
pip install -r requirements.txt
```

## Running simulations
For running the simulations, we give the graph as input through a file. The file should be in the following format:
```
1st line consists of n, m, src, p, s, sims
    where n = number of nodes
          m = number of edges
          src = source node of the graph
          p = probability that a link is broken (p / n is taken as probability that a node fails)
          s = current input from the source in the corresponding electrical graph
          sims = number of simulations
          th = threshold to consider whether a value is small enough
          ma = maximum number of continuous iterations for which a value is less than threshold
next m lines each consist of two integers u and v
    each pair denotes an undirected unweighted edge in the graph
```
See `graph.txt` for an example.

Run the simulations with the following command:
```bash
python main.py {filename} {file_prefix}
```

{filename} is the file from which you want to read the graph and {file_prefix} is the prefix you want to use for saving network drawings in the images directory (this is automatically created).
