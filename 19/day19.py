from math import sqrt
import numpy as np

def norm(v):
    return sqrt(np.dot(v, v))

def isColinear(a, b):
    return abs(np.dot(a/norm(a), b/norm(b))) == 1
    
    

def isCoplanar(v1, v2, v3):

    perp = np.cross(v1, v2)

    return abs(np.dot(perp, v3)) < 0.0000001

def load_scanner_data(file_name):

    scanners = []
    f = open(file_name, "r")
    line = f.readline()
    scanner = []
    while line:
        #print("processing '{}'".format(line))
        if line[0:2] == '--':
            #print("--> start of new scanner")
            scanner = []
        elif line.isspace():
            #print("end of scanner data")
            scanners.append(scanner)
        else:
            tmp = np.array([int(x) for x in line.strip().split(",")])
            #print("--> found beacon data and parsed to tuple {}".format(tmp))
            scanner.append([norm(tmp), tmp])

        line = f.readline()
    
    f.close()
    return scanners

def find_point_basis(scanner):
    # basic plan:
    # for each beacon a0 in scanner data, attemp to find 3 other beacons (a1, a2, a3) that meet the following criteria
    # 1. The three vectors that begin at a0 and proceed to a1, a2 and a3 form a basis for R^3
    scanner.sort()

    bases = []

    i = 0
    while i < len(scanner):
        anchor = scanner[i][1]
        print("anchor {}: {}".format(i, anchor))
        vectors = [(norm(x[1] - anchor), x[1] - anchor) for x in scanner if not all(x[1] == anchor)]
        vectors.sort()
        #print("vectors:\n{}".format(vectors))
        # find 
        v1 = vectors[0][1]
        j = 1 
        while isColinear(v1, vectors[j][1]) and j < len(vectors):
            j += 1
        
        if j >= len(vectors):
            continue

        v2 = vectors[j][1]
        j += 1

        while isCoplanar(v1, v2, vectors[j][1]) and j < len(vectors):
            j += 1

        if j >= len(vectors):
            continue
        
        v3 = vectors[j][1]
        m = np.transpose(np.array([v1, v2, v3]))

        bases.append([np.linalg.det(m), m, anchor])
        i += 1
    return bases

if __name__ == "__main__":

    scanners = load_scanner_data("example")

    pt1 = np.array([1, 0, 0])
    pt2 = np.array([0, 1, 0])
    pt3 = np.array([0, 0, 1])
    pt4 = np.array([2, 0, 0])

    print("Are these colinear: {} (Should be false)".format(isColinear(pt1, pt2)))
    print("Are these colinear: {} (Should be true)".format(isColinear(pt1, pt4)))

    # for beacon in scanners[0]:
    #     print(beacon)

    scanner_0_bases = find_point_basis(scanners[0])
    scanner_1_bases = find_point_basis(scanners[1])

#    scanner_0_bases.sort()
    
#    scanner_1_bases.sort()

    print(scanner_0_bases[0])
    print("Looking for matches")

    
    for s0 in scanner_0_bases:
        for s1 in scanner_1_bases:
            if abs(abs(s0[0]) - abs(s1[0])) < 0.000001:
                print("Found Match!!!")
                print("From s0:\ndet: {}; mat: {}".format(s0[0], s0[1]))
                print("From s1:\ndet: {}; mat: {}".format(s1[0], s1[1]))
                break

    T = np.matmul(s0[1], np.linalg.inv(s1[1]))

    print(T)

    # then take all beacons from scanner 1. and Create vectors that are anchored at [14, -140, 941].
    # Next apply Transform T to vectors created in previous step. This will give us vectors anchored at [14, 154, -927] 
    #   with the same orientation as scanner 0
    # Finally add [14, 154, -927] to get the position of all points relative to scanner 0
    # Should now remove duplicates before repeating process for scanner 2 to N.
    # 
    # Other thoughts. Consider instead of using T directly. Seeing which rotation matrix matches this.               