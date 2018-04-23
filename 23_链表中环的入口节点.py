class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_loop(head):
    """
    判断一个链表是否有环，有的话返回环中的节点个数

    @return (bool， int)
    """
    if head is None:
        return False, None

    p1 = head
    p2 = head
    while True:
        # p1一次走两步
        for _ in range(2):
            if p1.next is None:
                return False, None
            p1 = p1.next
        # p2一次走一步
        p2 = p2.next
        if p2 == p1:
            break

    # 走到这里一定有环
    # p2不动， p1一步一步走，直到p1与p2重合得出环中节点个数
    num_of_loop = 0
    while True:
        p1 = p1.next
        num_of_loop += 1
        if p1 == p2:
            return True, num_of_loop


def find_entry_of_loop(head):
    has_loop, num_of_node = find_loop(head)
    if not has_loop:
        return None

    p1 = head
    p2 = head
    for _ in range(num_of_node):
        p1 = p1.next

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1


if __name__ == "__main__":
    l1_6 = Node(6)
    l1_5 = Node(5, l1_6)
    l1_4 = Node(4, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    l1_6.next = l1_5
    head = l1_1
    print(find_entry_of_loop(head).value)

