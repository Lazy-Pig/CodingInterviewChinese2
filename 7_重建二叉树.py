class TreeNode(object):
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


def create_tree(preorder, inorder):
    if not isinstance(preorder, list) or not isinstance(inorder, list) or \
            len(preorder) != len(inorder):
        return

    for x, y in zip(preorder, inorder):
        if not isinstance(x, int) or not isinstance(y, int):
            return

    # 检查两个序列是否有重复值，以及两个序列包含的元素是否相同
    preorder_set = set(preorder)
    inorder_set = set(inorder)
    if preorder_set != inorder_set or len(preorder_set) != len(preorder) or \
            len(inorder_set) != len(inorder):
        return

    root = create_tree_recursively(preorder=preorder, inorder=inorder)
    return root


def create_tree_recursively(preorder, inorder):
    # 如果不满足说明不是两个序列不是同一棵树的前序遍历和中序遍历
    assert set(preorder) == set(inorder)

    if len(preorder) == 0:
        return None

    root = TreeNode(preorder[0])
    root_index = inorder.index(preorder[0])
    root.left_child = create_tree_recursively(preorder=preorder[1:root_index + 1],
                                              inorder=inorder[:root_index])
    root.right_child = create_tree_recursively(preorder=preorder[root_index + 1:],
                                               inorder=inorder[root_index + 1:])
    return root


def print_level(node, position_name):
    if node is None:
        return
    print_level(node.left_child, "left")
    print_level(node.right_child, "right")
    print()
    print(position_name, " ", node.data, end=' ')


if __name__ == "__main__":
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    root = create_tree(preorder=preorder, inorder=inorder)
    print_level(root, "root")

