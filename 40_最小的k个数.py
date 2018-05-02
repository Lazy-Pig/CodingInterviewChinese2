import random
"""
解法一：时间复杂度为O(n)的算法，只有当我们可以修改输入的数组时可用
"""


def partitaion(array, start, end):
    if not isinstance(array, list) or not isinstance(start, int) or not isinstance(end, int) or \
            start < 0 or end > len(array) - 1:
        return

    pivot = random.randint(start, end)
    array[pivot], array[start] = array[start], array[pivot]

    left = start + 1
    right = end
    while True:
        while left <= right and array[left] < array[start]:
            left += 1

        while left <= right and array[right] > array[start]:
            right -= 1

        if left > right:
            break
        array[left], array[right] = array[right], array[left]
    array[start], array[right] = array[right], array[start]
    return right


def get_least_numbers1(array, k):
    if not isinstance(array, list) or len(array) == 0 or not isinstance(k, int) or k <= 0 or k > len(array):
        return

    start = 0
    end = len(array) - 1
    index = partitaion(array, start, end)
    while index is not None and index != k - 1:
        if index > k - 1:
            end = index - 1
        else:
            start = index + 1
        index = partitaion(array, start, end)

    if index is None:
        return

    for i in range(k):
        print(array[i], end=" ")
    print()


"""
解法二：时间复杂度为O(nlogk)的算法， 特别适合处理海量数据
（不改变原数组）
"""


def get_least_numbers2(array, k):
    import heapq

    max_heap = []
    for x in array:
        heapq.heappush(max_heap, -x)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    for x in max_heap:
        print(-x, end=" ")
    print()


if __name__ == "__main__":
    get_least_numbers1([4, 5, 1, 6, 2, 7, 3, 8], 4)

