import day03

report = day03.load_report("input")

rates = day03.calc_rates(report)

print("Part 1 answers:")
print("The rates (in binary) are gamma: {}; and epsilon: {}".format(rates[0], rates[1]))

gamma = day03.bin2dec(rates[0])
epsilon = day03.bin2dec(rates[1])
        
print("The rates (in decimal) are gamma: {}; and epsilon: {}".format(gamma, epsilon))

print("Power consumption is {} * {} = {}". format(gamma, epsilon, gamma * epsilon))