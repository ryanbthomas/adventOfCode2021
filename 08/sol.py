import day08

data = day08.read_input("input")

total_found = day08.count_uniqs(data)

print("Part1: found {} 1, 4, 7, or 8s in outputs".format(total_found))

print("Part2:")


total = 0
for i in range(len(data)):
    seg_map = day08.create_seg_map(data[i][0])
    digits = ''.join(day08.sevenseg2bin(day08.apply_seg_map(seg_map, data[i][1])))
    print("{}: {}".format(i, digits))
    total += int(digits)

print("total: {}".format(total))  