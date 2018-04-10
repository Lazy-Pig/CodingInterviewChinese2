class TreeNode(object):
    def __init__(self, data, parent=None, left_child=None, right_child=None):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


def set_relation(parent, left_child, right_child):
    parent.left_child = left_child
    parent.right_child = right_child
    left_child.parent = parent
    right_child.parent = parent


def find_next_node_in_inordered1(node):
    """
    给定树中的一个节点，返回该节点在中序遍历中的下一个节点
    """
    if node is None:
        return None

    # 有右子树，返回右子树中的最左边的节点
    if node.right_child:
        next_node = node.right_child
        while next_node.left_child:
            next_node = next_node.left_child
        return next_node

    # 没有右子树，有父节点
    if node.parent:
        parent = node.parent

        # 节点是父节点的左子节点，返回父节点
        if id(node) == id(parent.left_child):
            return parent

        # 节点是父节点的右子节点，返回是左子节点的祖先节点的父节点
        if id(node) == id(parent.right_child):
            while parent.parent:
                if id(parent) == id(parent.parent.left_child):
                    return parent.parent
                parent = parent.parent
    return None


if __name__ == "__main__":
    node_i = TreeNode("i")
    node_h = TreeNode("h")
    node_g = TreeNode("g")
    node_f = TreeNode("f")
    node_e = TreeNode("e")
    node_d = TreeNode("d")
    node_c = TreeNode("c")
    node_b = TreeNode("b")
    node_a = TreeNode("a")
    set_relation(node_e, node_h, node_i)
    set_relation(node_c, node_f, node_g)
    set_relation(node_b, node_d, node_e)
    set_relation(node_a, node_b, node_c)

    print(find_next_node_in_inordered1(node_i).data)
