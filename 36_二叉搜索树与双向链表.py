class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def covert_tree_to_link(root):
    if not isinstance(root, TreeNode):
        return

    last_node = None
    last_node = covert_core(root, last_node)

    while last_node and last_node.left_child:
        last_node = last_node.left_child
    display(last_node)


def covert_core(current_node, last_node):
    if current_node is None:
        return

    if current_node.left_child:
        last_node = covert_core(current_node.left_child, last_node)

    if last_node:
        last_node.right_child = current_node
        current_node.left_child = last_node
    last_node = current_node

    if current_node.right_child:
        last_node = covert_core(current_node.right_child, last_node)
    return last_node


def display(head):
    p = head
    while p:
        print(p.value, end=" ")
        if p.left_child:
            print(p.left_child.value, end=" ")
        if p.right_child:
            print(p.right_child.value, end=" ")
        print()
        p = p.right_child


if __name__ == "__main__":
    node7 = TreeNode(16)
    node6 = TreeNode(12)
    node5 = TreeNode(8)
    node4 = TreeNode(4)
    node3 = TreeNode(14, left_child=node6, right_child=node7)
    node2 = TreeNode(6, left_child=node4, right_child=node5)
    node1 = TreeNode(10, left_child=node2, right_child=node3)
    root = node1
    covert_tree_to_link(root)
