import day13
import numpy as np

(paper, folds) = day13.load_input("input")

print("folds: \n{}".format(folds))

action = {
    'x': (lambda x : day13.fold_hort(paper, int(x))),
    'y': (lambda y : day13.fold_vert(paper, int(y)))
    }

(dim, line) = folds[0]

paper = action[dim](line)

(ycnt, xcnt) = np.where(paper == "#")

print("part 1: number of #: {}".format(len(xcnt)))

for (dim, line) in folds[1:]:
    paper = action[dim](line)

for r in paper:
    row_str = ''
    for c in r:
        row_str += c
        if c == '':
            row_str += ' '
    print(row_str)
