import numpy as np

def load_input(file_name):
    f = open(file_name, "r")

    out = []
    line = f.readline()
    while line:
        out.append(list(map(int, list(line[0:-1]))))
        line = f.readline()
    f.close()

    return np.array(out) 

def find_lowpoints(data):
    
    idx = np.ones_like(data, dtype = bool)
    
    # look right
    idx[:, 0:-1] *= data[:, 0:-1] < data[:, 1:]
    # look left
    idx[:, 1:] *= data[:, 1:] < data[:, 0:-1]
    # look up
    idx[0:-1, :] *= data[0:-1, :] < data[1:, :]
    # look down
    idx[1:, :] *= data[1:, :] < data[0:-1, :]
    

    return data[idx], convert_to_list(np.where(idx))

def score_risklevel(low_points):
    return(sum([x + 1 for x in low_points]))

def convert_to_list(lower_points):
    out = []
    for i in range(len(lower_points[0])):
        out.append((lower_points[0][i], lower_points[1][i]))
    return out

def flow_to_low_point(pt, data, low_points):
    if pt in low_points:
        #print("found low point {}".format(pt))
        return [pt]
    
    row = pt[0]
    col = pt[1]
    
    up = data[(pt[0] - 1, pt[1])] if pt[0] > 0 else 9
    down = data[(pt[0] + 1, pt[1])] if pt[0] < data.shape[0] -1 else 9
    left = data[(pt[0], pt[1] - 1)] if pt[1] > 0 else 9
    right = data[(pt[0], pt[1] +1)] if pt[1] < data.shape[1] -1 else 9

    opts = {
        up: (pt[0] -1, pt[1]),
        down: (pt[0] + 1, pt[1]),
        left: (pt[0], pt[1] -1),
        right: (pt[0], pt[1] + 1)

    }
    #print("From {}, my opts: {}".format(pt, opts))
    keys = opts.keys()
    out = [pt]
    out.extend(flow_to_low_point(opts[min(keys)], data, low_points))
    return out
    
        

def find_basins(data, low_points):
    basin_grid = np.zeros_like(data)
    nines_idx = convert_to_list(np.where(data == 9))
    for i in nines_idx:
        basin_grid[i] = -1
    
    open_pos = convert_to_list(np.where(basin_grid == 0))
    
    while len(open_pos) > 0:
        chain_flow = flow_to_low_point(open_pos[0], data, low_points)
        
        val = low_points.index(chain_flow[-1]) + 1
        #print("chain: {} |-> {}".format(chain_flow, val))
        for i in chain_flow:
            basin_grid[i] = val
        
        open_pos = convert_to_list(np.where(basin_grid == 0))

    return basin_grid

def calc_basin_sizes(basin_grid):
    out = []
    basin_grid = list(basin_grid.flatten())
    for i in range(1, max(basin_grid) + 1):
        
        out.append(basin_grid.count(i))
    
    return out

if __name__ == "__main__":

    data = load_input("example")

    print("here's the data")

    for i in data:
        print("{}".format(i))

    (low_points, low_point_loc) = find_lowpoints(data)

    print("low points: \n{}".format(low_points))

    print("risk level: {}".format(score_risklevel(low_points)))

    # check flow point

    print("flow from (3,2):\n {}".format(flow_to_low_point((3,2),data, low_point_loc)))
    print("flow from (0, 4):\n {}".format(flow_to_low_point((0,4),data, low_point_loc)))

    print("basin grid")
    basin_grid = find_basins(data, low_point_loc)

    print(basin_grid)

    basin_sizes = calc_basin_sizes(basin_grid)
    print("count basin size {}".format(basin_sizes))

    

    

