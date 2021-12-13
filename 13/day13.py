import numpy as np

def load_input(file_name):

    f = open(file_name, "r")
    dots = []
    folds = []
    max_y = 0
    max_x = 0
    line = f.readline().strip()
    # this will go to blank line    
    while line:
        (c, r) = line.split(",")
        max_y = max(int(r), max_y)
        max_x = max(int(c), max_x)
        dots.append((int(r), int(c)))
        line = f.readline().strip()
    
    # now get the folds
    line = f.readline().strip()
    while line:
        (dim, line_num) = line[11:].split("=")
        folds.append((dim, line_num))
        line = f.readline().strip()
    f.close()

    paper = np.empty(shape = (max_y + 1, max_x +1), dtype = str)

    while dots:
        pt = dots.pop()
        paper[pt] = '#'
    
    return paper, folds

def fold_vert(paper, line):

    top = paper[0:line, :]
    bottom = paper[line+1:, :]

    new_paper = top
    if top.shape[0] < bottom.shape[0]:
        new_paper = np.empty_like(bottom)
        new_paper[-line:, :] = top

    for i in range(bottom.shape[0]):

        old_line = new_paper[line - i -1]
        from_bottom = bottom[i]
        new_line = [max(old_line[x], from_bottom[x]) for x in range(len(old_line))]        

        new_paper[line - i - 1, :] = new_line

    return new_paper

def fold_hort(paper, line):
    tmp = fold_vert(paper.transpose(), line)
    return tmp.transpose()

if __name__ == "__main__":

    (paper, folds) = load_input("example")

    print("paper:")
    for r in paper:
        print("{}".format(r))
    
    print("folds:\n{}".format(folds))

    new_paper = fold_vert(paper, 7)

    print("new_paper:")
    for r in new_paper:
        print("{}".format(r))    
    
    final_paper = fold_hort(new_paper, 5)

    print("new_paper:")
    for r in final_paper:
        print("{}".format(r)) 

    (ycnt, xcnt) = np.where(new_paper == '#')

    print("number of #: {}".format(len(xcnt)))   