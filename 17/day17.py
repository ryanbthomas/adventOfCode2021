from math import ceil, floor, sqrt

def load_input(file_name):
    f = open(file_name, "r")
    line = f.read().strip()
    f.close()

    (x_data, y_data) = line[13:].split(", ")

    x_target_data = [int(x) for x in x_data[2:].split("..")]
    y_target_data = [int(y) for y in y_data[2:].split("..")]
    x_target_data.sort()
    y_target_data.sort()
    return x_target_data, y_target_data

# code from https://www.geeksforgeeks.org/check-whether-given-point-lies-inside-rectangle-not/
# A utility function to calculate 
# area of triangle formed by (x1, y1), 
# (x2, y2) and (x3, y3) 
def area(x1, y1, x2, y2, x3, y3):
      
    return abs((x1 * (y2 - y3) + 
                x2 * (y3 - y1) + 
                x3 * (y1 - y2)) / 2.0)
  
# A function to check whether point 
# P(x, y) lies inside the rectangle 
# formed by A(x1, y1), B(x2, y2), 
# C(x3, y3) and D(x4, y4) 
def check(x1, y1, x2, y2, x3, 
          y3, x4, y4, x, y):
                
    # Calculate area of rectangle ABCD 
    A = (area(x1, y1, x2, y2, x3, y3) +
         area(x1, y1, x4, y4, x3, y3))
  
    # Calculate area of triangle PAB 
    A1 = area(x, y, x1, y1, x2, y2)
  
    # Calculate area of triangle PBC 
    A2 = area(x, y, x2, y2, x3, y3)
  
    # Calculate area of triangle PCD 
    A3 = area(x, y, x3, y3, x4, y4)
  
    # Calculate area of triangle PAD 
    A4 = area(x, y, x1, y1, x4, y4);
  
    # Check if sum of A1, A2, A3 
    # and A4 is same as A 
    return (A == A1 + A2 + A3 + A4)

def generate_grid(target_data):

    (x_data, y_data) = target_data

    grid = []

    min_x = ceil(0.5 * (-1 + sqrt(1 + 8* x_data[0])))
    max_x = floor(0.5 * (-1 + sqrt(1 + 8 * x_data[1])))
    print("x range: {} to {}".format(min_x, x_data[1]))
    print("y range: {} to {}".format(0, abs(min(y_data))-1))

    for x in range(min_x, x_data[1] + 1):
        for y in range(min(y_data), abs(min(y_data))+ 1):
            #print("adding ({},{})".format(x, y))
            grid.append((x, y))
    
    return grid


def fire_probe(target_data, pt):

    vx,vy = pt

    x,y = 0,0
    steps = 0
    while x <= target_data[0][1] and y >= target_data[1][0]:
        x += vx
        y += vy
        vx -= 1 if vx > 0 else 0
        vy -= 1
        steps += 1
        if check(target_data[0][0], target_data[1][1], target_data[0][1], target_data[1][1], target_data[0][1], target_data[1][0], target_data[0][0], target_data[1][0], x, y):
            print("steps: {}; lands: {}".format(steps, (x, y)))
            return ['hit', pt[1] * (pt[1] + 1) / 2]
    return ['miss']




if __name__ == "__main__":
    target_data = load_input("example")

    print("target_data: {}".format(target_data))

    search_grid = generate_grid(target_data)

    #print(search_grid)

    print("check solutions:\n")
    max_height = 0
    max_height_pt = None
    all_hits = []
    for pt in search_grid:
        result = fire_probe(target_data, pt)
        if result[0] == 'hit':
            all_hits.append(pt)
            print("hit from {}; max @ {}".format(pt, result[1])) 
            if max_height < result[1]:
                max_height = result[1]
                max_height_pt = pt

    
    print("Max height: {} @ {}".format(max_height, pt))
    
    print("Number of successful init trajectories: {}".format(len(all_hits)))

