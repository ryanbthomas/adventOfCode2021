import day09
import math
data = day09.load_input("input")

print("Part 1")

(low_points, low_point_loc) = day09.find_lowpoints(data)

print("low points: \n{}".format(low_points))
print("risk level: {}".format(day09.score_risklevel(low_points)))

print("Part 2")

basin_grid = day09.find_basins(data, low_point_loc)


basin_sizes = day09.calc_basin_sizes(basin_grid)
basin_sizes.sort(reverse = True)

print("count basin size {}".format(basin_sizes))


print("Product of the 3 largest are {}".format(math.prod(basin_sizes[0:3])))
