class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_first_common_node(head1, head2):
    if not isinstance(head1, Node) or not isinstance(head2, Node):
        return

    len1 = get_list_length(head1)
    len2 = get_list_length(head2)

    if len1 > len2:
        long_p = head1
        short_p = head2
        delta = len1 - len2
    else:
        long_p = head2
        short_p = head1
        delta = len2 - len1

    while delta:
        long_p = long_p.next
        delta -= 1

    while long_p and short_p:
        if long_p.value == short_p.value:
            return long_p.value

        long_p = long_p.next
        short_p = short_p.next
    return None


def get_list_length(head):
    if not isinstance(head, Node):
        return 0

    length = 0
    p = head
    while p:
        length += 1
        p = p.next
    return length


if __name__ == "__main__":
    node7 = Node(7)
    node6 = Node(6, node7)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    head2 = node4

    node3 = Node(3, node6)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    head1 = node1
    print(find_first_common_node(head1, head2))
