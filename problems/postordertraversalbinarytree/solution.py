class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def solve(tree):
    stack, order = [tree], []
    while stack:
        node = stack.pop(-1)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
        seen.append(node.value)
    return seen[::-1]

#   Tree:
#     4
#    / \
#   1   5
#  / \   \
# 7   3   6
tree = Node(4, Node(1, Node(7), Node(3)), Node(5, right=Node(6)))
print(*solve(tree), sep=" ")
