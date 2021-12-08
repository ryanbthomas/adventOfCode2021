
import day07

f = open("input", "r")

init = list(map(int, f.readline().split(",")))

cheap_pos = day07.find_cheapest_position(init)
total_fuel = sum([abs(x-cheap_pos) for x in init])
print("Best position is {}; Total fuel {}.".format(cheap_pos, total_fuel))