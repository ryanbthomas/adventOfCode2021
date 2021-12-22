import day17


target_data = day17.load_input("input")

print("target_data: {}".format(target_data))

search_grid = day17.generate_grid(target_data)

#print(search_grid)

print("check solutions:\n")
max_height = 0
max_height_pt = None
all_hits = []
for pt in search_grid:
    result = day17.fire_probe(target_data, pt)
    if result[0] == 'hit':
        all_hits.append(pt)
        print("hit from {}; max @ {}".format(pt, result[1])) 
        if max_height < result[1]:
            max_height = result[1]
            max_height_pt = pt


print("Max height: {} @ {}".format(max_height, pt))

print("Number of successful init trajectories: {}".format(len(all_hits)))
    