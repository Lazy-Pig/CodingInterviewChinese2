import sys
from queue import Queue


class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def serialize(root):
    if root is None:
        return

    sys.stdout.write(str(root.value))
    if root.left_child:
        serialize(root.left_child)
    else:
        sys.stdout.write('$')

    if root.right_child:
        serialize(root.right_child)
    else:
        sys.stdout.write('$')


def deserialize(list_of_char):
    if not isinstance(list_of_char, list) or len(list_of_char) == 0:
        return

    if list_of_char[0] == '$':
        node = None
    else:
        node = TreeNode(int(list_of_char[0]))
    list_of_char.pop(0)
    if node:
        node.left_child = deserialize(list_of_char)
        node.right_child = deserialize(list_of_char)
    return node


def print_tree_from_top_to_bottom2(root):
    """
    题目二： 分行从上到下打印二叉树
    """
    if root is None:
        return
    assert isinstance(root, TreeNode)

    node_queue = Queue()
    node_queue.put(root)
    n_node = 1
    next_n_node = 0
    while not node_queue.empty():
        node = node_queue.get()
        print(node.value, end=' ')

        if node.left_child:
            next_n_node += 1
            node_queue.put(node.left_child)

        if node.right_child:
            next_n_node += 1
            node_queue.put(node.right_child)

        n_node -= 1
        if n_node == 0:
            print()
            n_node = next_n_node
            next_n_node = 0


if __name__ == "__main__":
    node6 = TreeNode(6)
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node5, node6)
    node2 = TreeNode(2, node4)
    node1 = TreeNode(1, node2, node3)
    root = node1
    serialize(root)
    print()
    new_root = deserialize(['1','2','4','$','$','$','3','5','$','$','6','$','$'])
    print_tree_from_top_to_bottom2(new_root)
