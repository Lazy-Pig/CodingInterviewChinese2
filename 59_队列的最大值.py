from collections import deque


"""
题目一： 滑动窗口的最大值
"""


def max_in_windows(array, win_size):
    if not isinstance(array, list) or len(array) == 0 or win_size < 1 or win_size > len(array):
        return

    max_of_window = []
    index_deque = deque()

    for i in range(win_size):
        while len(index_deque) != 0 and array[index_deque[-1]] < array[i]:
            index_deque.pop()
        index_deque.append(i)

    for i in range(win_size, len(array)):
        max_of_window.append(array[index_deque[0]])
        while len(index_deque) != 0 and array[i] > array[index_deque[-1]]:
            index_deque.pop()

        while len(index_deque) != 0 and index_deque[0] <= i - win_size:
            index_deque.popleft()

        index_deque.append(i)
    max_of_window.append(array[index_deque[0]])
    return max_of_window


"""
题目二： 队列的最大值
"""


class QueueWithMax(object):
    def __init__(self):
        self.data = deque()
        self.max_queue = deque()
        self.current_index = 0

    def push_back(self, num):
        while len(self.max_queue) != 0 and num >= self.max_queue[-1][1]:
            self.max_queue.pop()
        self.max_queue.append((self.current_index, num))
        self.data.append((self.current_index, num))
        self.current_index += 1

    def pop_front(self):
        assert len(self.data) != 0
        index, num = self.data.popleft()
        if index == self.max_queue[0][0]:
            self.max_queue.popleft()

    def max(self):
        assert len(self.data) != 0
        return self.max_queue[0][1]


if __name__ == "__main__":
    print(max_in_windows([2, 3, 4, 2, 6, 2, 5, 1], 3))
    q = QueueWithMax()
    q.push_back(3)
    print(q.max_queue)
    q.push_back(1)
    print(q.max_queue)
    q.push_back(2)
    print(q.max_queue)
    q.pop_front()
    print(q.max_queue)
    q.pop_front()
    print(q.max_queue)
