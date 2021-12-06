import numpy as np
import re

def load_input(file_name, cond = lambda x: True):
    f = open(file_name, "r")
    lines = []
    max_dims = (0, 0)
    p = re.compile("\d+")
    line = f.readline()
    while line:
        nums = list(map(int, p.findall(line)))
        pts = [(nums[i + 1], nums[i]) for i in (0, 2)]
        line = f.readline()
        if not cond(pts):
            continue
        lines.append(pts)
        max_dims = (max(pts[0][0], pts[1][0], max_dims[0]), max(pts[0][1], pts[1][1], max_dims[1]))
    f.close()
    max_dims = (max_dims[0] + 1, max_dims[1] + 1)
    return lines, max_dims

def gen_line_pts(ends):
    rise = ends[1][0] - ends[0][0]
    vert_step = 1 if rise >=0 else -1
    run = ends[1][1] - ends[0][1]
    hort_step = 1 if run >= 0 else -1
    #print("rise: {}; run: {}".format(rise, run))
    line_pts = []
    for i in range(0, run + hort_step, hort_step):
        for j in range(0, rise + vert_step, vert_step):
            pt = (ends[0][0] + j, ends[0][1] + i)
            #print("rise: {}; run: {}; pt: {}".format(rise, run, pt))
            if abs(run) < 0.01 or abs(pt[0] - (rise/run * (pt[1] - ends[0][1]) + ends[0][0])) < 0.01: 
            #check:
            #    print("+ {}".format(pt)) 
                line_pts.append(pt)
    
    return line_pts

def make_vent_map(line_segs, max_dims):
    grid = np.zeros(shape = max_dims)
    
    for i in range(len(line_segs)):
        print(line_segs[i])
        line_set_pts = gen_line_pts(line_segs[i])
        for pt in line_set_pts:
            grid[pt] += 1
    return grid

if __name__ == "__main__":
    print("Load data")

    (line_segs,max_dims) = load_input("example_input")
    print("max_dims: {}".format(max_dims))
    for i in range(len(line_segs)):
        print(line_segs[i])
    
    print("Load data for only vert and hort lines")

    no_diag = lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1]

    (line_segs, max_dims) = load_input("example_input", cond = no_diag)
    print("max_dims: {}".format(max_dims))
    for i in range(len(line_segs)):
        print(line_segs[i])
    
    grid = make_vent_map(line_segs, max_dims) 
    print("final grid")
    print(grid)

    idx = grid[:,:] >= 2

    print("The number of dangerous points is {}".format(idx.sum()))
    print("Part 2 test")
    print("Load data for only vert and hort lines")


    (line_segs, max_dims) = load_input("example_input")
    print("max_dims: {}".format(max_dims))
    
    for i in range(len(line_segs)):
        print(line_segs[i])
    grid = make_vent_map(line_segs, max_dims) 
    
    print("final grid")
    print(grid)

    idx = grid[:,:] >= 2

    print("The number of dangerous points is {}".format(idx.sum()))