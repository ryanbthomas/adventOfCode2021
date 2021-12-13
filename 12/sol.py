import day12

g = day12.load_graph("input")

paths = []
start = ('start',)

day12.find_paths(start, g, paths)

print("Part 1: I found {} paths.".format(len(paths)))

paths = []
start = ('start',)

day12.find_paths2(start, g, paths)

print("Part 2: I found {} paths.".format(len(paths)))