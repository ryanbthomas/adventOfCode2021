import day16

bits = day16.load_input("input")

parsed_packets = day16.parse_packet(bits)

def sum_version_num(p):

    if p[1] == 4:
        # if literal value return version number
        return p[0]
    
    sub_total = 0
    for s in p[2]:
        sub_total += sum_version_num(s)
    
    return p[0] + sub_total

sum_of_version_nums = sum_version_num(parsed_packets)

print("Part 1:\nSum of version numbers: {}".format(sum_of_version_nums))

packet_value = day16.eval_bits(parsed_packets)

print("Part2:\n packet value is {}".format(packet_value))