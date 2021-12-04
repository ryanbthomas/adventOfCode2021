
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

# funcs for part 2
def find_o2_rating(report):
    num_rows = report.shape[0] 
    print("num_rows: {}".format(num_rows))   
    
    if num_rows == 1:
        return report

    on_bit_counts = report.sum(axis = 0)[0]
    print("on_bit_counts: {}".format(on_bit_counts))

    bit_val = int(on_bit_counts >= (num_rows / 2))
    print("bit_val: {}".format(bit_val))
    idx = report[:, 0] == bit_val
    return np.column_stack((bit_val, find_o2_rating(report[idx, 1:])))

def find_co2_rating(report):
    num_rows = report.shape[0] 
    print("num_rows: {}".format(num_rows))   
    
    if num_rows == 1:
        return report

    on_bit_counts = report.sum(axis = 0)[0]
    print("on_bit_counts: {}".format(on_bit_counts))

    least_common_bit_val = 1 - int(on_bit_counts >= (num_rows / 2))
    print("least common bit_val: {}".format(least_common_bit_val))
    idx = report[:, 0] == least_common_bit_val
    return np.column_stack((least_common_bit_val, find_co2_rating(report[idx, 1:])))


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

    print("Let's check the o^2 calculation")

    oxygen_bin = find_o2_rating(report)
    oxygen = bin2dec(oxygen_bin.flatten())
    print("The oxygen generator rating is {} (binary) {}".format(oxygen_bin.flatten(), oxygen))

    if oxygen == 23:
        print("Well done!")
    else:
        print("Oops!")

    print("Let's check the co^2 calculation")

    co2_bin = find_co2_rating(report)
    co2 = bin2dec(co2_bin.flatten())
    print("The co^2 scrubber rating is {} (binary) {}".format(co2_bin.flatten(), co2))

    if co2 == 10:
        print("Well done!")
    else:
        print("Oops!")




