
def move_sub(start, direction, units):
    if direction == "forward":
        return (start[0] + units, start[1])
    
    sign = 1
    if direction == "up":
        sign = -1
    
    return (start[0], start[1] + sign * units)

def move_sub2(start, direction, units):
    #start is now (hort, vert, aim)
    if direction == "forward":
        return (start[0] + units, start[1] + start[2]*units, start[2])
    
    sign = 1
    if direction == "up":
        sign = -1
    
    return (start[0], start[1], start[2] + sign * units)


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

def move_to_final_pos(move, start_pos, directions, units):
    
    for i in range(len(directions)):
        new_pos = move(start_pos, directions[i], units[i])
        print("Move sub from {} {} {} units -> {}".format(start_pos, directions[i], units[i], new_pos))        
        start_pos = new_pos
    
    return(new_pos)

if __name__ == "__main__":

    print("Check to see if load_commands works")
    (d, u) = load_commands("example")

    print("directions: {}".format(d))
    print("units: {}".format(u))

    print("Check to see if we can move the sub")
    pos = move_to_final_pos(move_sub, (0, 0), d, u)
    print ("The final position is {}".format(pos))

    print("Check to see if we can move the sub using method 2")
    pos = move_to_final_pos(move_sub2, (0, 0, 0), d, u)
    print ("The final position is {}".format(pos))
    