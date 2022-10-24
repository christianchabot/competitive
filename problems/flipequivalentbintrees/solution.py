class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

roots = [
#      roots[0][0]   roots[0][1]
#     /     \       /     \
#    2       3     3       2
#   / \     /       \     / \
#  4   5   6         6   4   5
#     / \                   / \
#    7   8                 8   7
    [
        Node(Node(Node(), Node(Node(), Node())), Node(Node())), 
        Node(Node(right=Node()), Node(Node(), Node(Node(), Node())))
    ],
#    roots[1][0]   roots[1][1]
#   /                   \
#  2                     2
#                       /
#                      3
    [
        Node(Node()),
        Node(right=Node(Node()))
    ],
#    roots[2][0]   roots[2][1]
#   /             /
#  2             2
    [
        Node(Node()),
        Node(Node())
    ]
]

def solve(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif (tree1 is None and tree2 is not None) or (tree1 is not None and tree2 is None):
        return False

    return ((solve(tree1.left, tree2.left) and solve(tree1.right, tree2.right)) or
            (solve(tree1.left, tree2.right) and solve(tree1.right, tree2.left)))

print(solve(roots[0][0], roots[0][1]))
print(solve(roots[1][0], roots[1][1]))
print(solve(roots[2][0], roots[2][1]))
