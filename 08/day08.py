def find_unique_digits(input):
    uniqs = dict()
    cnt = 0
    uniq_map = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }
    for str in input:
        num = len(str)
        if num in [2, 4, 3, 7]:
            cnt += 1
            lst = list(str)
            lst.sort()
            uniqs[uniq_map[num]] = lst
    
    return uniqs, cnt

def read_input(file_name):
    
    f = open(file_name, "r")
    data = []
    line = f.readline()
    while line:
        tmp = line.split()
        data.append([tmp[0:10], tmp[11:]]) 
        line = f.readline()
    f.close()
    return data

def count_uniqs(data, pos = 1):
    total_found = 0
    for i in data:
        (uniqs, cnt) = find_unique_digits(i[pos])
        #print(uniqs)
        #print("Adding {}".format(cnt))
        total_found += cnt 
    return total_found

def sevenseg2bin(x):
    lookup = {
        'abcefg':  '0',
        'cf':      '1',
        'acdeg':   '2',
        'acdfg':   '3',
        'bcdf':    '4',
        'abdfg':   '5',
        'abdefg':  '6',
        'acf':     '7',
        'abcdefg': '8',
        'abcdfg':  '9'
    }

    out = []
    if not isinstance(x[0], list):
        x = [x] 

    for v in x:
        out.append(lookup[''.join(v)])

    return out    

def create_seg_map(x):
    single_list = list(''.join(x)) 
    seg_map = {}

    # 97 to 103 |-> 'a' to 'g'
    for seg in range(97, 104):
        count = single_list.count(chr(seg))
        if count == 6:
            seg_map[chr(seg)] = 'b'
        elif count == 4:
            seg_map[chr(seg)] = 'e'
        elif count == 9:
            seg_map[chr(seg)] = 'f'

    # let's find digits we're sure about 
    (uniq_digits, ignore) = find_unique_digits(x)    
    
    #1
    idx = [x in seg_map.keys() for x in uniq_digits[1]]
    seg_map[uniq_digits[1][idx.index(False)]] = 'c'
    #4
    idx = [x in seg_map.keys() for x in uniq_digits[4]]
    seg_map[uniq_digits[4][idx.index(False)]] = 'd'
    #7
    idx = [x in seg_map.keys() for x in uniq_digits[7]]
    seg_map[uniq_digits[7][idx.index(False)]] = 'a'
    #8
    idx = [x in seg_map.keys() for x in uniq_digits[8]]
    seg_map[uniq_digits[8][idx.index(False)]] = 'g'

    return seg_map 

def apply_seg_map(seg_map, input):
    out = []

    for num in input:
        tmp = []
    #    print("num: {}".format(num))
        for i in num:
    #        print("{} |-> {}".format(i, seg_map[i]))
            tmp.append(seg_map[i])
        tmp.sort()
        out.append(tmp)
    return out 

if __name__ == "__main__":

    data = read_input("example")
    for i in data:
        print("{} |-> {}".format(i[0], i[1]))

    total_found = count_uniqs(data)    
    print("Found {} 1, 4, 7 or 8s".format(total_found))

    seg_map = create_seg_map(data[0][0])

    print(seg_map)

    total = 0
    for i in range(len(data)):
        seg_map = create_seg_map(data[i][0])
        digits = ''.join(sevenseg2bin(apply_seg_map(seg_map, data[i][1])))
        print("{}: {}".format(i, digits))
        total += int(digits)

    print("total: {}".format(total))  