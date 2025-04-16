def pre_order(node):
    if node is None:
        return []
    res = []
    res.append(node.data)
    if node.left:
        res += (pre_order(node.left))
    if node.right:
        res += (pre_order(node.right))
    return res
