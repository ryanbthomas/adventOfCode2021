
import day01

f = open("input", "r")

input= list(map(int, f.read().split("\n")))

f.close()

rolling_avgs = day01.create_rolling_window(input)

print("The number of depth increases is {}".format(day01.find_depth_increases(rolling_avgs)))
