import day06

f = open("input", "r")
school = list(map(int, f.readline().split(",")))
f.close()

exp1 = day06.run_experiment(school, 80)

print("Part1: Found {} fish after 80 days.".format(exp1))
exp2 = day06.run_experiment(school, 256)
print("Part2: found {} fish after 256 days.".format(exp2))