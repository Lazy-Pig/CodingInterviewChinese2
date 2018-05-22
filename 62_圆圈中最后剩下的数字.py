"""
解法一：用循环链表
时间O(mn)，空间O(n)
"""


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def last_remaining(n, m):
    if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
        return

    next = None
    for i in range(n - 1, -1, -1):
        node = Node(value=i, next=next)
        if i == n - 1:
            last = node
        next = node
    head = next
    last.next = head
    pre = last
    p = head
    while id(p) != id(p.next):
        for _ in range(m - 1):
            pre = p
            p = p.next
        pre.next = p.next
        p = pre.next
    return p.value


if __name__ == "__main__":
    print(last_remaining(5, 3))
