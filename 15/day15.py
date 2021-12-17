
def calc_adjacent_vertices(pt, rows, cols):

    d = {(-1, 0), (0, 1), (1, 0), (0,-1)}
    adj_vertices = []
    for dr, dc in d:
        new_pt = (pt[0] + dr, pt[1] + dc)
        if 0 <= new_pt[0] < rows and 0 <= new_pt[1] < cols:
            adj_vertices.append(new_pt)

    return adj_vertices


def load_input(file_name):

    f = open(file_name, "r")

    # first read into list:

    lines = f.read().split()
    f.close()

    num_rows = len(lines)
    num_cols = len(lines[0])

    all_pts = [(r, c) for r in range(num_rows) for c in range(num_cols)]

    graph = dict()

    for pt in all_pts:
        graph[pt] = calc_adjacent_vertices(pt, num_rows, num_cols)

    return graph