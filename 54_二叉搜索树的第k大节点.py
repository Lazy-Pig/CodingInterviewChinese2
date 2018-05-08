class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def kth_node(root, k):
    if not isinstance(root, TreeNode) or k == 0:
        return None

    _, result = kth_node_core(root, k)
    return result


def kth_node_core(root, k):
    if root is None:
        return k, None

    k, value = kth_node_core(root.left_child, k)

    if value:
        return k, value

    if k == 1:
        return k, root.value

    k -= 1
    return kth_node_core(root.right_child, k)


if __name__ == "__main__":
    node8 = TreeNode(8)
    node6 = TreeNode(6)
    node4 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(3, node2, node4)
    node7 = TreeNode(7, node6, node8)
    node5 = TreeNode(5, node3, node7)
    root = node5

    print(kth_node(root, 3))
