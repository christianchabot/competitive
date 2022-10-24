class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def solve(graph):
    seen = [] # Hash table of seen nodes.
    def recurse(graph):
        nonlocal seen
        ret = []
        for child in graph.children:
            if child not in seen:
                ret += recurse(child)
                seen += [child]
        return ret + [graph.val]
    return recurse(graph)

#     Tree:
#      0
#     / \
#    1   2
#   / \   \
#  3   4   5
tree = Node(0, [Node(1, [Node(3), Node(4)]), Node(2, [Node(5)])])
print(*solve(tree), sep=" ")
