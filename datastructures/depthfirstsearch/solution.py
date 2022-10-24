class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def solve(graph):
    order, seen, stack = [], [], [graph]
    while stack:
        node = stack.pop(-1)
        for child in node.children:
            if child not in seen:
                stack += [child]
                seen += [child]
        order += [node.val]
    return order[::-1]

#     Tree:
#      0
#     / \
#    1   2
#   / \   \
#  3   4   5
tree = Node(0, [Node(1, [Node(3), Node(4)]), Node(2, [Node(5)])])
print(*solve(tree), sep=" ")
