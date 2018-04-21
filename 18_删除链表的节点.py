class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def delete_node(head_p, delete_p):
    """
    题目一：O(1)时间内删除链表节点
    """
    if head_p is None or delete_p is None:
        return

    # 只有一个节点
    if head_p == delete_p and delete_p.next is None:
        head_p = None
        return head_p

    # 删除的节点是尾节点
    if delete_p.next is None:
        p = head_p
        while p.next != delete_p:
            p = p.next
        p.next = delete_p.next
        return head_p

    # 一般节点，把待删除节点的下一节点的内容复制到待删除节点中，就相当于删除了这个节点
    next_node = delete_p.next
    delete_p.value = next_node.value
    delete_p.next = next_node.next
    return head_p


def delete_duplicated_node(head):
    """
    题目二：删除链表中重复的节点
    """
    if head is None or head.next is None:
        return head

    new_head = Node(-1)
    new_p = new_head
    old_p = head

    while old_p and old_p.next:
        if old_p.value == old_p.next.value:
            delete_value = old_p.value
            while old_p and old_p.value == delete_value:
                old_p = old_p.next
            new_p.next = old_p
        else:
            new_p.next = old_p
            new_p = new_p.next
            old_p = old_p.next
    return new_head.next


if __name__ == "__main__":
    # l1_5 = Node(10)
    # l1_4 = Node(7, l1_5)
    # l1_3 = Node(5, l1_4)
    # l1_2 = Node(2, l1_3)
    # l1_1 = Node(1, l1_2)
    # head_p = delete_node(l1_1, l1_2)
    #
    # while head_p is not None:
    #     print(head_p.value)
    #     head_p = head_p.next

    l1_7 = Node(5)
    l1_6 = Node(4, l1_7)
    l1_5 = Node(4, l1_6)
    l1_4 = Node(3, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head = l1_1
    head_p = delete_duplicated_node(head)

    while head_p is not None:
        print(head_p.value)
        head_p = head_p.next
