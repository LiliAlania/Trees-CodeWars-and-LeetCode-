from collections import deque
def tree_by_levels(node):
    if node is None:
        return []
    res = []
    queue = deque([node])
