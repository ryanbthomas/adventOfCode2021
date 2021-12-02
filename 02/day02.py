
def move_sub(start, direction, units):
    if direction == "forward":
        return (start[0] + units, start[1])
    
    sign = 1
    if direction == "up":
        sign = -1
    
    return (start[0], start[1] + sign * units)


def load_commands(input_file):
    f = open(input_file, "r")

    directions = []
    units = []

    line = f.readline()

    while line:
        (d, u) = line.split()
        directions.append(d)
        units.append(int(u))
        line = f.readline()

    return directions, units

if __name__ == "__main__":

    print("Check to see if load_commands works")
    (d, u) = load_commands("example")

    print("directions: {}".format(d))
    print("units: {}".format(u))

    print("Check to see if we can move the sub")
    pos = (0, 0)
    for i in range(len(d)):
        new_pos = move_sub(pos, d[i], u[i])
        print("Move sub from {} {} {} units -> {}".format(pos, d[i], u[i], new_pos))        
        pos = new_pos
    
    print ("The final position is {}".format(pos))