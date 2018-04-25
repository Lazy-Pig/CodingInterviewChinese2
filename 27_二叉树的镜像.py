class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def mirror_recursivly(root):
    if root is None:
        return

    if root.left_child is None and root.right_child is None:
        return

    root.left_child, root.right_child = root.right_child, root.left_child
    mirror_recursivly(root.left_child)
    mirror_recursivly(root.right_child)


def print_tree(root):
    if root is None:
        return

    print(root.value)
    print_tree(root.left_child)
    print_tree(root.right_child)


if __name__ == "__main__":
    node7 = TreeNode(value=11)
    node6 = TreeNode(value=9)
    node5 = TreeNode(value=7)
    node4 = TreeNode(value=5)
    node3 = TreeNode(value=10, left_child=node6, right_child=node7)
    node2 = TreeNode(value=6, left_child=node4, right_child=node5)
    node1 = TreeNode(value=8, left_child=node2, right_child=node3)
    root = node1
    print_tree(root)
    print()
    mirror_recursivly(root)
    print_tree(root)
