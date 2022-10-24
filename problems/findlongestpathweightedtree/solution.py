class Node:
    def __init__(self, weight, children=[]):
        self.weight = weight
        self.children = children

# Because this is a tree structure we do not need to keep track of seen nodes.
def solve(tree):
    stack, weights = [(tree.weight, tree)], []
    while stack:
        weight, node = stack.pop(-1)
        for child in node.children[::-1]:
            stack.append((child.weight + node.weight, child))
        weights.append(weight)
    return max(weights)

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
