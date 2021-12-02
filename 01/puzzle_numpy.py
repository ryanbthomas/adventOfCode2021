import numpy as np
import day01


input= np.loadtxt("input", dtype = int)


print("Part 1")

part1_ans = sum(np.diff(input) > 0)
print("The number of depth increases is {}".format(part1_ans))


print("Part 2")
#rolling_avgs = day01.create_rolling_window(input)
part2_ans = sum(np.diff(input, n = 3) > 0)
print("The number of depth increases is {}".format(part2_ans))
