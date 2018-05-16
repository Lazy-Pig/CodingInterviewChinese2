class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

"""
题目一：二叉树深度 
"""


def tree_depth(root):
    if not isinstance(root, TreeNode):
        return 0

    n_left = tree_depth(root.left_child)
    n_right = tree_depth(root.right_child)
    return max(n_left, n_right) + 1


"""
题目二： 平衡二叉树
"""


def is_balanced(root):
    if root is None:
        return True, 0

    left_is_balanced, left_depth = is_balanced(root.left_child)
    right_is_balanced, right_depth = is_balanced(root.right_child)
    if left_is_balanced and right_is_balanced and left_depth - right_depth in (-1, 0, 1):
        depth = left_depth + 1 if left_depth > right_depth else right_depth + 1
        return True, depth

    return False, None


if __name__ == "__main__":
    node7 = TreeNode(7)
    node6 = TreeNode(6)
    node5 = TreeNode(5, node7)
    node4 = TreeNode(4)
    node3 = TreeNode(3, None, node6)
    node2 = TreeNode(2, node4, node5)
    node1 = TreeNode(1, node2, node3)
    root = node1

    print(tree_depth(root))

    print(is_balanced(root))
