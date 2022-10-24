class Node:
    def __init__(self, weight, children=[]):
        self.weight = weight
        self.children = children

def solve(tree):
    return tree.weight+max([solve(node) for node in tree.children] + [0])

#      Tree:
#        A
#       / \
#      4   3
#     /     \
#    B       C
#    |      /|\
#    2     4 2 1
#    |    /  |  \
#    D   E   F   G
#            |
#            1
#            |
#            H
tree = Node(0, [Node(4, [Node(2)]), Node(3, [Node(4), Node(2, [Node(1)]), Node(1)])])
print(solve(tree))
