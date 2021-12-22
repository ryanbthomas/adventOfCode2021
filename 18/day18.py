
# refactor
# create node class
# node is either endpoint or container
# endpoint has values
# container has pointer to another node
# node has pointer to parent
# we will create a binary tree
# add: create a new node, left points to first operand in sum and the rigth points to the second
# split: search tree for number >= 10. Replace with with new node with values that follow split algo
# explode: search tree for depth >= 4, keeping track of point to right most node on the left with a real value; when explosion occurs
#       we go back to parent to find left most node to the right with real value to update
# magnitude: tree traversal; recursive algo until real values found 
# from_str: use stack to track '[' and pop when you find closing ']' and build up tree structure.
class sfnum:

    def __init__(self, x, max_depth = 0, max_value = None):
        self.num = x
        self.max_depth = max_depth
        if max_value == None:
            self.max_value = max(x)
                
    def isReduced(self):
        return self.max_depth < 4 and self.max_value < 10

    def reduce(x):
        # steps to reduce snailfish num
        while not x.isReduced():
            if x.max_depth >= 4:
                x = sfnum.explode(x)
            elif x.max_value >= 10:
                x = sfnum.split(x)

        return x

    def explode(x):
        # find first
         
    def from_str(s):
        # parse nested array from str
        # 
        sfn = sfnum([])

        return sfn
    
    def __add__(self, o):
        # return a new object
        new_max_depth = max(self.max_depth, o.max_depth) + 1
        new_max_value = max(self.max_value, o.max_value)
        sfn = sfnum.reduce(sfnum([self.num, o.num], max_depth= new_max_depth, max_value= new_max_value))

        return sfn

    def magnitude(x):
        if isinstance(x, int):
            return x

        return 3 * sfnum.magnitude(x[0]) + 2 * sfnum.magnitude(x[1]) 


