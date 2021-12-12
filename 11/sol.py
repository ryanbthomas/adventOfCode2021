import day11

data = day11.load_data("input")
orig_data = data.copy()

print("Orig Data: ")
day11.pretty_print(data)

print("Simulating 100 steps")

total_flashes = day11.sim_flashes(data, steps = 100)

print("Part 1: Found {} flashes".format(total_flashes))

data = orig_data.copy()

num_steps = 0
while data.sum() > 0:
    total_flashes = day11.sim_flashes(data)
    num_steps+=1

print("Part 2: Syncronized in {} steps".format(num_steps))