import day14
import numpy as np
from numpy.linalg import matrix_power

(first_letter, labels, pt, g) = day14.load_input2("input")

print("Part 1: ")

part_1 = np.matmul(matrix_power(g, 10), pt)

cnts = day14.count_letters(part_1, labels, first_letter)

print(cnts)
print("score: {}".format(max(cnts.values()) - min(cnts.values())))

print("Part 2: ")

part_2 = np.matmul(matrix_power(g, 40), pt)

cnts = day14.count_letters(part_2, labels, first_letter)

print(cnts)
print("score: {}".format(max(cnts.values()) - min(cnts.values())))
