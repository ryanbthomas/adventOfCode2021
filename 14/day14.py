from collections import defaultdict

import numpy as np
from numpy.linalg import matrix_power

# naive solution originally used to answer part 1

def load_input(file_name):
    f = open(file_name, "r")

    polymer_template = f.readline().strip()
    #skip blank link
    f.readline()

    insert_rules = defaultdict(lambda x: '')

    line = f.readline().strip()

    while line:
        (pair, new) = line.split(" -> ")
        insert_rules[pair] = new
        line = f.readline().strip()

    f.close()

    return polymer_template, insert_rules


def grow_polymer(polymer, insert_rules, steps = 1):
    #print("Template: {}".format(polymer))
    for s in range(steps):
        i = 0
        while i < len(polymer) - 1:
            
            new_base = insert_rules[polymer[i:i+2]]
            #print("** Looking up {} and found {}. Inserting between {} and {}".format(polymer[i:i+2], new_base, polymer[:i+1],  polymer[i+1:]))
            polymer = polymer[:i+1] + new_base + polymer[i+1:]
            i+=2
        print("step {} done.".format(s + 1))
    return polymer

def grow_polymer_df(polymer, insert_rules, steps = 1):
    # stop condition
    if steps == 0:
        return polymer
    # split into pairs
    
    pairs = [polymer[x:x+2] for x in range(0, len(polymer)-1)]
    #print("pairs: {}".format(pairs))
    new_polymer = []
    
    for p in pairs:
        p_new = p[0] + insert_rules[p] + p[1]
    #    print("{} |-> {} and so becomes {}".format(p, insert_rules[p], p_new))
        new_polymer.append(grow_polymer_df(p_new, insert_rules, steps -1))
    
    #print("new_polymer: {}".format(new_polymer))
    return new_polymer[0] + ''.join([s[1:] for s in new_polymer[1:]])

def score_polymer(polymer):
    cnts = [polymer.count(x) for x in set(polymer)]
    cnts.sort()
    return cnts[-1] - cnts[0]


# more efficient solution necessary to solve part 2

def load_input2(file_name):
    f = open(file_name, "r")

    template_str = f.readline().strip()
    template_list = [template_str[x:x+2] for x in range(len(template_str)-1)]

    #skip blank link
    f.readline()
    d = dict()

    line = f.readline().strip()

    #gotta read it in first so we know what the possible keys are
    while line:
        (pair, new) = line.split(" -> ")
        d[pair] = [pair[0] + new, new + pair[1]]
        line = f.readline().strip()

    f.close()

    labels = list(d.keys())

    template = np.array([template_list.count(k) for k in labels])
    template.shape = (len(labels), 1)
    growth = np.zeros(shape = (len(labels), len(labels)))

    for k in d.keys():
        n = d[k]
        growth[labels.index(n[0]), labels.index(k)] += 1
        growth[labels.index(n[1]), labels.index(k)] += 1          


    return template_str[0], labels, template, growth

def count_letters(v, labels, start):
    cnts = {k:0 for k in set(''.join(labels))}
    cnts[start] += 1
    for b in labels:
        cnts[b[1]] += v[labels.index(b), 0]

    return cnts

if __name__ == "__main__":

    (start_letter, labels, template, growth) = load_input2("example")

    
    print("Check Example")
    print("labels: {}".format(labels))
    print("template: \n{}".format(template))
    print("growth:")
    for r in growth:
        print(r)

    t1 = np.matmul(matrix_power(growth, 10), template)
    print(np.transpose(t1))
    cnts = count_letters(t1, labels, start_letter)
    print(cnts)
    print("score: {}".format(max(cnts.values()) - min(cnts.values())))

    t2 = np.matmul(matrix_power(growth, 40), template)
    print(np.transpose(t2))
    cnts = count_letters(t2, labels, start_letter)

    print(cnts)

    print("score: {}".format(max(cnts.values()) - min(cnts.values())))