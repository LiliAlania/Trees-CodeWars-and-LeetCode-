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

def in_order(node):
    if node is None:
        return []
    res = []
    if node.left:
        res += in_order(node.left)
    res.append(node.data)
    if node.right:
        res += in_order(node.right)
    return res
    
def post_order(node):
    res = []
    if node is None:
        return []
    if node.left:
        res += post_order(node.left)
    if node.right:
        res += post_order(node.right)
    res.append(node.data)
    return res
