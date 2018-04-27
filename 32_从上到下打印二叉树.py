from queue import Queue


class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def print_tree_from_top_to_bottom1(root):
    """
    题目一： 不分行从上倒下打印二叉树
    """
    if root is None:
        return

    assert isinstance(root, TreeNode)
    node_queue = Queue()
    node_queue.put(root)

    while not node_queue.empty():
        node = node_queue.get()
        if node.left_child:
            node_queue.put(node.left_child)

        if node.right_child:
            node_queue.put(node.right_child)

        print(node.value, end=' ')


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


def print_tree_from_top_to_bottom3(root):
    if root is None:
        return

    assert isinstance(root, TreeNode)
    stack1 = []
    stack2 = []
    stack1.append(root)
    level = 1

    while len(stack1) != 0 or len(stack2) != 0:
        if level & 1:
            current_stack = stack1
            next_stack = stack2
        else:
            current_stack = stack2
            next_stack = stack1

        while len(current_stack) != 0:
            node = current_stack.pop()
            print(node.value, end=' ')
            if level & 1:
                if node.left_child:
                    next_stack.append(node.left_child)

                if node.right_child:
                    next_stack.append(node.right_child)
            else:
                if node.right_child:
                    next_stack.append(node.right_child)

                if node.left_child:
                    next_stack.append(node.left_child)
        print()
        level += 1


if __name__ == "__main__":
    node7 = TreeNode(11)
    node6 = TreeNode(9)
    node5 = TreeNode(7)
    node4 = TreeNode(5)
    node3 = TreeNode(10, left_child=node6, right_child=node7)
    node2 = TreeNode(6, left_child=node4, right_child=node5)
    node1 = TreeNode(8, left_child=node2, right_child=node3)
    root = node1
    print_tree_from_top_to_bottom3(root)
