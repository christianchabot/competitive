T = 3
n, k, h = 9, 2, 2
a = [6, 7, 11, 1, 12, 15, 4, 6, 10]
nodes = [(1, 2), (1, 3), (2, 4), (2, 6), (3, 5), (6, 7), (6, 8), (5, 9)]

#         Tree
#        1(6)
#       /  \
#   (7)2    3(11)
#     / \     \
# (1)4   6(15) 5(12)
#       /  \    \
#   (4)7   8(6) 9(10)

# Select k nodes that are at least h distance apart and maximizes the sum.

# How to solve:
# 1. Could construct a tree from the nodes.
# 2. 
