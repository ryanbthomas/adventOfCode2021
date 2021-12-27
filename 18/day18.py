
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

class node:

    def __init__(self, left, right):

        if isinstance(left, node):
            left.parent = self
            left.side = 'left'

        if isinstance(right, node):    
            right.parent = self
            right.side = 'right'

        self.left = left
        self.right = right
        self.parent = None
        self.side = None
        self.next_left = None
        self.next_right = None
    
    def setNextLeft(self, o, side):
        self.next_left = [o, side]
    
    def setNextRight(self, o, side):
        self.next_right = [o, side]
    
    def getLeftMostNumberNode(self):
        if isinstance(self.left, int):
            return [self, 'left']
        
        return self.left.getLeftMostNumberNode()
    
    def getRightMostNumberNode(self):
        if isinstance(self.right, int):
            return [self, 'right']
        
        return self.right.getLeftMostNumberNode()

    #def rebalance(self):

    def from_str(s):
        
        p = []

        for c in s:
            if c == ',':
                continue
            elif c == ']':
                right = p.pop()
                left = p.pop()
                (nr, side) = left.getRightMostNumberNode()
                right.setNextLeft(nr, side)
                (nl, side) = right.getLeftMostNumberNode()
                left.setNextRight(nl, side)

                p.pop() # lose opening '['
                new_node = node(left, right)
                p.append(new_node)
            elif c == '[':
                p.append(c)    
            else:
                p.append(int(c))

        return p.pop()                

        
    


# class sfnum:

#     def __init__(self, tree = None):
#         self.tree = tree 

#     def rebalance(n):

#         if n.left == None:
#             if n.parent.right == n:
#                 n.parent.right = n.right
#             else:
#                 n.parent.left = n.right
        
#         if n.right == None:
#             if n.parent.right == n:
#                 n.parent.right = n.left
#             else:
#                 n.parent.left = n.left
        
#         if isinstance(n.left, node):
#             sfnum.rebalance(n.left)
#         if isinstance(n.right, node):
#             sfnum.rebalance(n.right)
            
#     def isReduced(self):
#         return self.max_depth < 4 and self.max_value < 10

#     def reduce(self):
#         # steps to reduce snailfish num
#         while not x.isReduced():
#             if x.max_depth >= 4:
#                 x = sfnum.explode(x)
#             elif x.max_value >= 10:
#                 x = sfnum.split(x)

#         return x

#     # def find_parent_next_right(n):

#     #     if n.parent.right == n:
#     #         return sfnum.find_parent_next_right(n.parent)
        
#     #     if isinstance(n.parent.right, int):
#     #         return n.parent



#     def explode_next(x, depth = 0):
#         # find first
#         if isinstance(x.left, node) and sfnum.explode_next(x.left, depth = depth + 1):
#             return True
#         if isinstance(x.right, node) and sfnum.explode_next(x.right, depth = depth + 1):
#             return True
#         # if we're here we're at a regular number node
#         if depth >= 4:
#             # we gonna explode
#             left_node = x.next_regular_left
#             right_node = x.next_regular_right
#             if not left_node == None:
#                 if isinstance(left_node.right, int):
#                     left_node.right += x.left
#                 else:
#                     left_node.left += x.left
#             if not right_node == None:
#                 if isinstance(right_node.left, int):
#                     right_node.left += x.right
#                 else:
#                     right_node.right += x.right
                
            
#     def from_str(s):
#         # parse nested array from str
#         # 
#         sfn = sfnum([])

#         return sfn
    
#     def __add__(self, o):
#         # return a new object
#         new_max_depth = max(self.max_depth, o.max_depth) + 1
#         new_max_value = max(self.max_value, o.max_value)
#         sfn = sfnum.reduce(sfnum([self.num, o.num], max_depth= new_max_depth, max_value= new_max_value))

#         return sfn

#     def magnitude(x):
#         if isinstance(x, int):
#             return x

#         return 3 * sfnum.magnitude(x[0]) + 2 * sfnum.magnitude(x[1]) 


