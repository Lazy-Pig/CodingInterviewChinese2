class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def is_symmetrical(root):
    return is_symmetrical_core(root, root)


def is_symmetrical_core(node1, node2):
    if node1 is None and node2 is None:
        return True

    if node1 is None or node2 is None:
        return False

    if node1.value != node2.value:
        return False

    return is_symmetrical_core(node1.left_child, node2.right_child) and \
        is_symmetrical_core(node1.right_child, node2.left_child)


if __name__ == "__main__":
    # node7 = TreeNode(5)
    # node6 = TreeNode(7)
    # node5 = TreeNode(7)
    # node4 = TreeNode(5)
    # node3 = TreeNode(6, left_child=node6, right_child=node7)
    # node2 = TreeNode(6, left_child=node4, right_child=node5)
    # node1 = TreeNode(8, left_child=node2, right_child=node3)
    # root = node1
    # print(is_symmetrical(root))

    # node6 = TreeNode(7)
    # node5 = TreeNode(7)
    # node4 = TreeNode(7)
    # node3 = TreeNode(7, left_child=node6)
    # node2 = TreeNode(7, left_child=node4, right_child=node5)
    # node1 = TreeNode(7, left_child=node2, right_child=node3)
    # root = node1
    # print(is_symmetrical(root))

    node7 = TreeNode(5)
    node6 = TreeNode(7)
    node5 = TreeNode(7)
    node4 = TreeNode(5)
    node3 = TreeNode(9, left_child=node6, right_child=node7)
    node2 = TreeNode(6, left_child=node4, right_child=node5)
    node1 = TreeNode(8, left_child=node2, right_child=node3)
    root = node1
    print(is_symmetrical(root))