class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_Kth_to_tail(head, k):
    if head is None or k == 0:
        return

    p1 = head
    p2 = head
    for _ in range(1, k):
        if p1.next is None:
            return
        p1 = p1.next

    while p1.next is not None:
        p1 = p1.next
        p2 = p2.next
    return p2


if __name__ == "__main__":
    l1_5 = Node(5)
    l1_4 = Node(4, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head = l1_1
    print(find_Kth_to_tail(head, 1).value)
