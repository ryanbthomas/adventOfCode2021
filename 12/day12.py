from collections import defaultdict

def load_graph(file_name):
    g = defaultdict(lambda : [])
    f = open(file_name, "r")
    line = f.readline().strip()

    while line:
        nodes = line.split("-")
        g[nodes[0]].append(nodes[1])
        if not (nodes[0] == 'start' or nodes[1] == 'end'):
            g[nodes[1]].append(nodes[0])
        line = f.readline().strip()

    f.close()

    return g

def find_paths(start, g, paths):

    for n in g[start[-1]]:
        if n == 'end':
            paths.append(start + (n,))
        elif n.isupper() or not n in start:
            find_paths(start + (n,), g, paths)

def small_cave_condition(start, n):
    # true if n not in start or if no small letter is in 2x
    if not n in start:
        return True
    
    if max([start.count(x) for x in set(start) if x.islower()]) < 2:
        return True
    
    return False

def find_paths2(start, g, paths):

    for n in g[start[-1]]:
        if n == 'end':
            paths.append(start + (n,))
        elif n.isupper() or small_cave_condition(start, n):
            find_paths2(start + (n,), g, paths)

def graph_pretty_print(g):
    for k in g.keys():
        print("{} |-> {}".format(k, g[k]))
    
if __name__ == "__main__":

    g = load_graph("example1")

    graph_pretty_print(g)

    paths = []

    start = ('start',)

    find_paths(start, g, paths)

    print("Example 1: I found {} paths:\n {}".format(len(paths), paths))
    
    g = load_graph("example2")

    graph_pretty_print(g)

    paths = []

    start = ('start',)

    find_paths(start, g, paths)

    print("Example 2: I found {} paths:\n {}".format(len(paths), paths))
    
    g = load_graph("example3")

    graph_pretty_print(g)

    paths = []

    start = ('start',)

    find_paths(start, g, paths)

    print("Example 3: I found {} paths.".format(len(paths)))

    print("Alt condition test")    
    g = load_graph("example1")
    paths = []
    start = ('start',)

    find_paths2(start, g, paths)

    print("Example 1: I found {} paths".format(len(paths)))
    
    g = load_graph("example2")
    paths = []
    start = ('start',)

    find_paths2(start, g, paths)

    print("Example 2: I found {} paths".format(len(paths)))
    
    g = load_graph("example3")
    paths = []
    start = ('start',)

    find_paths2(start, g, paths)

    print("Example 3: I found {} paths".format(len(paths)))