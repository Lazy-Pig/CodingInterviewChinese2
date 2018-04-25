class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def has_subtree(tree1, tree2):
    has = False
    if tree1 is None or tree2 is None:
        return has

    if tree1.value == tree2.value:
        has = dose_tree1_has_tree2(tree1, tree2)

    if not has:
        has = has_subtree(tree1.left_child, tree2)

    if not has:
        has = has_subtree(tree1.right_child, tree2)
    return has


def dose_tree1_has_tree2(tree1, tree2):
    if tree2 is None:
        return True

    if tree1 is None:
        return False

    if tree1.value != tree2.value:
        return False

    return dose_tree1_has_tree2(tree1.left_child, tree2.left_child) and \
           dose_tree1_has_tree2(tree1.right_child, tree2.right_child)


if __name__ == "__main__":
    tree1_7 = TreeNode(value=7)
    tree1_6 = TreeNode(value=4)
    tree1_5 = TreeNode(value=2, left_child=tree1_6, right_child=tree1_7)
    tree1_4 = TreeNode(value=9)
    tree1_3 = TreeNode(value=7)
    tree1_2 = TreeNode(value=8, left_child=tree1_4, right_child=tree1_5)
    tree1_1 = TreeNode(value=8, left_child=tree1_2, right_child=tree1_3)
    tree1 = tree1_1

    tree2_3 = TreeNode(2)
    tree2_2 = TreeNode(9)
    tree2_1 = TreeNode(8, left_child=tree2_2, right_child=tree2_3)
    tree2 = tree2_1

    print(has_subtree(tree1, tree2))
