import numpy as np
import day05

print("Part 1: ")
no_diag = lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1]

(line_segs, max_dims) = day05.load_input("input", cond = no_diag)
for i in range(len(line_segs)):
    print(line_segs[i])
print("max_dims: {}".format(max_dims))

grid = day05.make_vent_map(line_segs, max_dims) 
print("final grid")
print(grid)

idx = grid[:,:] >= 2

print("The number of dangerous points is {}".format(idx.sum()))

print("Part 2: ")

(line_segs, max_dims) = day05.load_input("input")
for i in range(len(line_segs)):
    print(line_segs[i])
print("max_dims: {}".format(max_dims))

grid = day05.make_vent_map(line_segs, max_dims) 
print("final grid")
print(grid)

idx = grid[:,:] >= 2

print("The number of dangerous points is {}".format(idx.sum()))