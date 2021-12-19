import day15


graph, costs = day15.load_input("input")

print("costs")
for r in costs:
    print(''.join([str(c) for c in r]))

(path, prev) = day15.find_lowest_risk((0, 0), graph, costs)

(num_row, num_col) = costs.shape
print("table is {} x {}".format(num_row, num_col))

print("Part 1:\nlowest cost path is {}".format(path[(num_row -1, num_col -1)]))

day15.print_path(prev, costs)

# part 2
graph, costs = day15.load_input("input", scale = day15.scale)

(path, prev) = day15.find_lowest_risk((0, 0), graph, costs)

(num_row, num_col) = costs.shape
print("table is {} x {}".format(num_row, num_col))

print("Part 2:\nlowest cost path is {}".format(path[(num_row -1, num_col -1)]))


#day15.print_path(prev, costs)
