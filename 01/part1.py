
import day01

f = open("input", "r")

input= list(map(int, f.read().split("\n")))

f.close()

print("The number of depth increases is {}".format(day01.find_depth_increases(input)))