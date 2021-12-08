import statistics as stat
def find_cheapest_position(init):
    # median minimizes the L1 norm
    init.sort()
    idx = len(init) // 2 if len(init) % 2 == 0 else len(init) // 2 + 1

    return init[idx]

def fuel_calc(init, pos):
    return sum([abs(x - pos) * (abs(x - pos) + 1)*0.5 for x in init])

def method_2(init):
    x_bar = stat.mean(init)
    x_sq_bar = stat.mean([x**2 for x in init])
    a = 3
    b = -(6 * x_bar + 2)
    c = 3 * x_sq_bar + 2 * x_bar
    descrim = (b**2 - 4 * a * c) ** 0.5
    sol = [(-b + descrim)/ (2*a), (-b - descrim)/ (2*a)]

    fuel = [fuel_calc(init, sol[0]), fuel_calc(init, sol[1])]

    if fuel[0] <= fuel[1]:
        return sol[0], fuel[0]
    
    return sol[1], fuel[1]
    

    


if __name__ == "__main__":
    init = [16,1,2,0,4,2,7,1,2,14]
    test = find_cheapest_position(init)
    if test == 2:
        print("Good job!")
    else:
        print("Oops! Expected 2 but got {}".format(test))
    
    (sol2, fuel2) = method_2(init)

    print("Part 2 check: pos {}, fuel {}".format(sol2, fuel2))