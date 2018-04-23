class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge_list(l1, l2):
    # 一个为None，就返回另一个
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    l = None
    head = l
    while l1 is not None and l2 is not None:
        if l1.value < l2.value:
            candidate_node = l1
            l1 = l1.next
        else:
            candidate_node = l2
            l2 = l2.next

        if l is None:
            l = candidate_node
            l.next = None
            head = l
        else:
            candidate_node.next = l.next
            l.next = candidate_node
            l = l.next
    if l1 is not None:
        l.next = l1

    if l2 is not None:
        l.next = l2
    return head


if __name__ == "__main__":
    l1_5 = Node(10)
    l1_4 = Node(7, l1_5)
    l1_3 = Node(5, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)

    l2_3 = Node(6)
    l2_2 = Node(6, l2_3)
    l2_1 = Node(5, l2_2)
    l1_1 = merge_list(l1_1, l2_1)

    while l1_1 is not None:
        print(l1_1.value)
        l1_1 = l1_1.next
