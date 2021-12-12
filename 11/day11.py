import numpy as np
from numpy.testing._private.utils import print_assert_equal

def load_data(file_name):

    f = open(file_name, "r")
    d = [[int(x) for x in r] for r in f.read().split()]
    f.close()
    return np.array(d)

def pretty_print(x):
    for r in x:
        print("{}".format(r))


def update_energy_level(x):
    if x == 0:
        return 0
    
    return x + 1

def sim_flashes(data, steps = 1): 
    total_flashed = 0
    d = {(r,c) for r in range(-1, 2) for c in range(-1, 2) if abs(r) + abs(c) != 0}
    for i in range(steps):
        print("Starting step {}".format(i + 1))
        data += 1
        (row, col) = np.where(data > 9)
        ready_to_flash = [(row[i], col[i]) for i in range(len(row))]
        flashed = []

        while ready_to_flash:
            pt = ready_to_flash.pop()
#            print("flashing {}".format(pt))
            data[pt] = 0
            flashed.append(pt)
            for dy, dx in d:
                # check
                if 0 <= pt[0] + dy < data.shape[0] and 0 <= pt[1] + dx < data.shape[1]:
                    new_pt = (pt[0] + dy, pt[1] + dx)
                    old_level = data[new_pt]
                    data[new_pt] = update_energy_level(data[new_pt])
#                    print("Updating level for {}: {} |-> {}".format(new_pt, old_level, data[new_pt]))
                    if data[new_pt] > 9 and (not new_pt in flashed and not new_pt in ready_to_flash):
#                        print("Adding {} to ready_to_flash".format(new_pt))
                        ready_to_flash.append(new_pt)

        total_flashed += len(flashed)

    return total_flashed

if __name__ == "__main__":

    data = load_data("example")
    orig_data = data.copy()

    print("example data:")
    pretty_print(data)

    print("Simulate 1 step")

    tot_flashes = sim_flashes(data)

    print("\nState:")
    pretty_print(data)
    print("Total # of flashes: {}".format(tot_flashes))

    print("Simulate 10 Steps:")

    data = orig_data.copy() 
    tot_flashes = sim_flashes(data, steps = 10)

    print("\nState:")
    pretty_print(data)
    print("Total # of flashes: {}".format(tot_flashes))
    
    print("Simulate 100 Steps:")

    data = orig_data.copy() 
    tot_flashes = sim_flashes(data, steps = 100)

    print("\nState:")
    pretty_print(data)
    print("Total # of flashes: {}".format(tot_flashes))