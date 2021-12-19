import numpy as np
import heapq as hq
import math

class bcolors:
    PATH = '\033[92m' #GREEN
    RESET = '\033[0m' #RESET COLOR


def calc_adjacent_vertices(pt, rows, cols):

    d = {(-1, 0), (0, 1), (1, 0), (0,-1)}
    adj_vertices = []
    for dr, dc in d:
        new_pt = (pt[0] + dr, pt[1] + dc)
        #print("check {} |-> {}".format(pt, new_pt))
        if 0 <= new_pt[0] < rows and 0 <= new_pt[1] < cols:
            adj_vertices.append(new_pt)

    return adj_vertices

def scale(x):

    # expand to right
    final_grid = x
    for i in range(4):
       x = x % 9 + 1
       final_grid = np.append(final_grid, x, axis = 1)

    y = final_grid 

    for i in range(4):
        y = y % 9 + 1
        final_grid = np.append(final_grid, y, axis = 0)
        
    
    return final_grid

def load_input(file_name, scale = lambda x: x):

    f = open(file_name, "r")

    # first read into list:

    lines = f.read().split()
    f.close()

    costs = scale(np.array([[int(x) for x in s] for s in lines]))

    (num_rows, num_cols) = costs.shape

    all_pts = [(r, c) for r in range(num_rows) for c in range(num_cols)]

    graph = dict()
    #print("rows: {}; cols: {}".format(num_rows, num_cols))
    for pt in all_pts:
        graph[pt] = calc_adjacent_vertices(pt, num_rows, num_cols)

    return graph, costs

def find_lowest_risk(start, graph, costs):
    cost,prev = {}, {}
    visited = set()

    for v in graph:
        cost[v] = math.inf
        prev[v] = None
    
    cost[start] = 0
    q = []
    hq.heappush(q, (0, start))

    while q:
        (tmp, u) = hq.heappop(q)
        visited.add(u)

        for v in graph[u]:
            if not v in visited:
                c = cost[u] + costs[v]
                if c < cost[v]:
                    cost[v] = c
                    prev[v] = u
                    hq.heappush(q, (cost[v], v))

    return cost, prev

def print_path(prev, costs):
    trek = []    
    (num_row, num_col) = costs.shape
    pt = (num_row -1, num_col -1)

    while pt != (0, 0):
        trek.append(pt)
        pt = prev[trek[-1]]

    tot = 0
    for r in range(costs.shape[0]):
        row_str = ''
        for c in range(costs.shape[1]):
            if (r,c) in trek:
                tot += costs[r, c]
                row_str += bcolors.PATH + str(costs[r,c]) + bcolors.RESET
            else:
                row_str += str(costs[r, c])
        print(row_str)

    print("total path cost: {}".format(tot))    






if __name__ == "__main__":

    graph, costs = load_input("example", scale = scale)

    
    (path,prev) = find_lowest_risk((0, 0), graph, costs)
    
    print_path(prev, costs)

    (num_row, num_col) = costs.shape

    print("lowest cost path is {}".format(path[(num_row -1, num_col -1)]))