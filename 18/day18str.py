import re

class sfnum:

    def __init__(self, s):
        self.str = s
    
    def __str__(self):
        return self.str

    def max_depth(self):
        max_depth = 0
        open_cnt = 0
        for s in self.str:
            if s == '[':
                open_cnt += 1
            elif s == ']':
                if open_cnt > max_depth:
                    max_depth = open_cnt
                open_cnt -= 1
            
        return max_depth
    
    def max_val(self):
        p = re.compile("\d+")

        return max([int(x) for x in p.findall(self.str)])

    def reduce(self):

        isReduced = False
        while not isReduced:
            if self.max_depth() >= 5:
                # explode
               # orig = str(self)
                self.explode()
                #print("exlode: {} |-> {}".format(orig, self))
            elif self.max_val() >= 10:
                #orig = str(self)
                self.split()
                #print("split: {} |-> {}".format(orig, self))
                # split
            else:
                isReduced = True

    def add_to_next_num(string, val, reverse = False):

        p = re.compile("\d+")
        
        # find next number to right
        next_num = p.search(string)
        if not next_num == None:

            next_val_str = string[next_num.start():next_num.end()]
            #print("next val str: {}".format(next_val_str))
            if reverse:
                next_val_str = next_val_str[-1::-1]
            #    print("--> reverse it: {}".format(next_val_str))
            
            next_val = val + int(next_val_str)
            #print("{} + {} = {}".format(val, int(next_val_str), next_val))

            next_val_str = str(next_val)
            #print("make it a string: {}".format(next_val_str))
            if reverse:
                next_val_str = next_val_str[-1::-1]
                #print("--> reverse it back: {}".format(next_val_str))

            string = string[:next_num.start()] + next_val_str + string[next_num.end():]
        
        return string
    
    def explode(self):
        # find the deepest first
        #deepest = self.max_depth()
        #print("deepest: {}".format(deepest))
        open_cnt = 0
        
        i = 0
        while open_cnt < 5:
            if self.str[i] == '[':
                open_cnt += 1
            elif self.str[i] == ']':
                open_cnt -= 1

            i+=1
        i = i-1

        j = 0
        while self.str[i+j] != ']':
            j+=1

        #p = re.compile("\[\d+,d+\]")
        #print("Searching in '{}'".format(self.str[i:]))
        #fnd = p.search(self.str[i:])
        #substr = self.str[i:][fnd.start():fnd.end()]
        substr = self.str[i:i+j+1]
        p2 = re.compile("\d+")
        vals = p2.findall(substr)
        
        right_side = sfnum.add_to_next_num(self.str[i+j+1:], int(vals[1]))

        left_side = sfnum.add_to_next_num(self.str[:i][-1::-1], int(vals[0]), reverse=True)

        self.str = left_side[-1::-1] + '0' + right_side

    def split(self):

        #max_val = self.max_val()
        p = re.compile("[1-9][0-9]+")
        srch = p.search(self.str)
        split_val = int(self.str[srch.start():srch.end()])
        left_val = split_val // 2
        right_val = split_val - left_val
        #print("split {} into [{}, {}]".format(split_val, left_val, right_val))
        split_val = sfnum.bracket(str(left_val), str(right_val))

        #p = re.compile(str(max_val))
        srch = p.search(self.str)
        self.str = self.str[:srch.start()] + split_val + self.str[srch.end():]
    
    def bracket(x, y):
        return '[' + x + ',' + y + ']'
    
    def __add__(self, o):

        return sfnum(sfnum.bracket(self.str, o.str))

    def magnitude(self):

        stack = []
        i = 0
        while i < len(self.str):

            if self.str[i].isdigit():
                j = 1
                while self.str[i + j].isdigit():
                    j+=1
                
                stack.append(int(self.str[i:i+j]))
            elif self.str[i] == ']':
                right_val = stack.pop()
                left_val = stack.pop()
                stack.append(3 * left_val + 2 * right_val)
            
            i += 1

        return stack.pop()

def sum_all_lines(file_name):

    f = open(file_name, "r")
    line = f.readline().strip()
    total = sfnum(line)
    line = f.readline().strip()
    while line:
        new_num = sfnum(line)
        print(" {}\n+{}".format(total, new_num))
        total = total + new_num
        total.reduce()
        print("={}\n".format(total))
        line = f.readline().strip()
    f.close()

    return total

if __name__ == "__main__":

    # print("Testing explode")

    # f = open("example_explode", "r")
    # line = f.readline().strip()

    # while line:
    #     print(line)
    #     (orig_num, expected) = line.split(" |-> ")
    #     tmp = sfnum(orig_num)
    #     tmp.explode()
    #     actual = tmp.str
    #     if actual == expected:
    #         print("    OK.")
    #     else:
    #         print("NOPE!!!!")
        
    #     line = f.readline().strip()

    # f.close()

    # print("Manually testing steps")

    # num1 = sfnum("[[[[4,3],4],4],[7,[[8,4],9]]]")
    # num2 = sfnum("[1,1]")

    # num3 = num1 + num2
    # print("num3: {}".format(num3))
    # num3.explode()
    # print("num3 after explode: {}".format(num3))
    # num3.explode()
    # print("num3 after explode: {}".format(num3))
    # num3.split()
    # print("num3 after split: {}".format(num3))
    # num3.split()
    # print("num3 after split: {}".format(num3))
    # num3.explode()
    # print("num3 after explode: {}".format(num3))

    # num4 = num1 + num2
    # num4.reduce()
    # print("num4 (orig num3 after reduce): {}".format(num4))

    # print("testing sum of lines")

    # test_num = sum_all_lines("example_sum01")

    # print("Test 01:\nFound {}\nShould be [[[[1,1],[2,2]],[3,3]],[4,4]]".format(test_num))
    
    # test_num = sum_all_lines("example_sum02")

    # print("Test 02:\nFound {}\nShould be [[[[3,0],[5,3]],[4,4]],[5,5]]".format(test_num))
    
    # test_num = sum_all_lines("example_sum04")

    # print("Test 04:\nFound {}\nShould be [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]".format(test_num))

    # f = open("example_magnitude", "r")

    # line = f.readline().strip()

    # while line:
    #     (input, mag) = line.split(" becomes ")
    #     num = sfnum(input)
    #     if num.magnitude() == int(mag):
    #         print("{}|->{}. OK.".format(input, mag))
    #     else:
    #         print("Oops!\n For {}, expected {} but found {}".format(input, mag, num.magnitude()))
    #     line = f.readline().strip()

    print("Final check")

    test_num = sum_all_lines("example")

    print("sfnum: {}\nmagnitude: {}".format(test_num, test_num.magnitude()))

