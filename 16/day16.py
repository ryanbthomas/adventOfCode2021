
def load_input(file_name):

    f = open(file_name, "r")
    d = {
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111"
    }

    bits = []
    for s in f.read().strip():
        bits.append(d[s])
    
    return ''.join(bits)

def strbin_to_dec(s):
    val = 0
    power = len(s) - 1
    for bit in s:
        val += int(bit) * 2 ** power
        power -= 1
    
    return val

def parse_packet_header(packet):
    version = strbin_to_dec(packet[0:3])
    type_ID = strbin_to_dec(packet[3:6])

    return version, type_ID

def parse_literal_value(packet):
    bits = packet[6:]
    print("packet: {}; non-header bits: {}".format(packet, bits))
    num = ''    
    for idx in range(0, len(bits), 5):
        num += bits[idx+1:idx+5]
        print("num: {}".format(num))
        if bits[idx] == '0':
            break
    return strbin_to_dec(num)

# def parse_operator_type0_packet(packet):
#     bits = packet[6:]

#     subpackets = []

#     while bits:
#         next_packet = find_whole_packet(bits)
#         (v, id) = parse_packet_header(next_packet)
#         subpackets.append()
#         bits = bits[len(next_packet):]


def bits_in_packet(packet):
    (v, id) = parse_packet_header(packet)

    if id == 4:
        i = 6
        while packet[i] == '1':
            i+=5
        tmp = i + 5
        #tmp += -tmp % 4
        return tmp
    
    if packet[6] == '0':
        #print("header: {} ({})".format(packet[0:6], len(packet[0:6])))
        #print("op type bit: {} (1)".format(packet[6]))
        bit_length = strbin_to_dec(packet[7:(7+15)])
        #print("subpacket bit length: {} ({}) |-> {}".format(packet[7:(7+15)], len(packet[7:(7+15)]), bit_length))
        #print("subpacket {} ({})".format(packet[(7+15):(7+15+bit_length)], len(packet[(7+15):(7+15+bit_length)])))
        #print("total packet: {}".format(packet[:(7+15+bit_length)]))

        return (7 + 15 + bit_length)
    
    if packet[6] == '1':
        num_packets = strbin_to_dec(packet[7:(7+11)])
        print("looking for {} packets".format(num_packets))
        total_bits = 7+11

        while num_packets > 0:
            print("checking: {}".format(packet[total_bits:]))
            next_packet = bits_in_packet(packet[total_bits:])
            print("identified packet: {}".format(packet[total_bits:(total_bits + next_packet)]))
            total_bits += next_packet
            num_packets-=1
        return total_bits
    
    ValueError("Something has gone wrong")

def parse_packet(packet):
    (v, id) = parse_packet_header(packet)

    if id == 4:
        return [v, id, parse_literal_value(packet)]
    
    subpacket_bit_length = 15
    if packet[6] == '1':
        subpacket_bit_length = 11    
    total_bits_in_packet = bits_in_packet(packet)
    print("total bits in packet: {}".format(total_bits_in_packet))
    subpackets = packet[(7+subpacket_bit_length):(total_bits_in_packet)]
    print("check bits in subpacket: {}".format(len(subpackets)))
    print("subpackets: {}".format(subpackets))
    subops = []
    while subpackets:
        bits = bits_in_packet(subpackets)
        print("bits is subpacket {}: {}".format(len(subops)+1, bits))
        print("subpacket: {}".format(subpackets[0:bits]))
        subops.append(parse_packet(subpackets[0:bits]))
        subpackets = subpackets[bits:]

    return [v, id, subops]
    
if __name__ == "__main__":

    bits = load_input("literal_value_example")


    print("Test strbin_to_dec")
    print("{} |-> {} (should be 5)".format("101", strbin_to_dec("101")))
    print("{} |-> {} (should be 25)".format("11001", strbin_to_dec("11001")))
    print("{} |-> {} (should be 64)".format("1000000", strbin_to_dec("1000000")))
    print("{} |-> {} (should be 10)".format("1010", strbin_to_dec("1010")))

    pkt = parse_packet(bits)
    print("literal value pkt: {}".format(pkt))

    bits = load_input("operator_0_example")
    pkt = parse_packet(bits)
    print("Operator 0 pkt: {}".format(pkt))

    bits = load_input("operator_1_example")
    print("full packet:\n{}".format(bits))
    pkt = parse_packet(bits)
    print("Operator 1 pkt: {}".format(pkt))

    #(v, id) = parse_packet_header(bits)

    #print("version: {}; type_id: {}".format(v, id))

    #val = parse_literal_value(bits)
    #print("Found val= {}".format(val))