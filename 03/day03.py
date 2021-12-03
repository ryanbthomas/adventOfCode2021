
import numpy as np

def load_report(file):
    f = open(file, "r")
    raw_data = f.readlines()
    num_rows = len(raw_data)
    num_bits = len(raw_data[0]) - 1
    # assumming alwasy 5 bit numbers
    report = np.zeros((num_rows, num_bits))

    for i in range(num_rows):
        for j in range(num_bits):
            report[i, j] = int(raw_data[i][j])

    return report

def bin2dec(x):
    powers = np.array([2**x for x in range(len(x) -1, -1, -1)])

    return(sum(x * powers))

def calc_rates(x):
    num_rows = x.shape[0]
    on_bit_counts = x.sum(axis = 0)

    gamma_rate = (on_bit_counts >= (num_rows // 2)) * 1
    epsilon_rate = 1 - gamma_rate

    return [gamma_rate, epsilon_rate]    


if __name__ == "__main__":

    print("Can I import data correctly?")

    report = load_report("example_input")

    print(report)

    rates = calc_rates(report)

    print("The rates (in binary) are gamma: {}; and epsilon: {}".format(rates[0], rates[1]))

    gamma = bin2dec(rates[0])
    epsilon = bin2dec(rates[1])
        
    print("The rates (in decimal) are gamma: {}; and epsilon: {}".format(gamma, epsilon))

    print("Power consumption is {} * {} = {}". format(gamma, epsilon, gamma * epsilon))

