
import day18str

print("Part 1")

test_num = day18str.sum_all_lines("input")

print("sfnum: {}\nmagnitude: {}".format(test_num, test_num.magnitude()))


print("Part 2")

print("Load all sfnums")

f = open("input", "r")

sfnums = [day18str.sfnum(l) for l in f.readlines()]

f.close()

print("length of sfnums: {}".format(len(sfnums)))
print("type of 0 entry: {}". format(type(sfnums[0])))
print("val of 0 entry: {}". format(sfnums[0]))

mags = []
for i in range(100):
    for j in [k for k in range(100) if k != i]:

        new_num = sfnums[i] + sfnums[j]
        new_num.reduce()
        mags.append(new_num.magnitude())

print("max mag sum is {}".format(max(mags)))
