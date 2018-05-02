import random
"""
解法一：基于Partition函数的时间复杂度为O(n)的算法
（即top n/2思想）
（修改原数组）
"""


def partition(array, start, end):
    if not isinstance(array, list) or not isinstance(start, int) or not isinstance(end, int) or \
            start < 0 or end >= len(array):
        return None

    pvit = random.randint(start, end)
    array[start], array[pvit] = array[pvit], array[start]

    left = start + 1
    right = end

    while True:
        while left <= right and array[left] <= array[start]:
            left += 1

        while left <= right and array[right] >= array[start]:
            right -= 1

        if left > right:
            break

        array[left], array[right] = array[right], array[left]
    array[start], array[right] = array[right], array[start]
    return right


def check_more_than_half(array, target):
    count = 0
    for x in array:
        if x == target:
            count += 1
    return count > len(array) / 2


def find_more_than_half_num1(array):
    if not isinstance(array, list) or len(array) == 0:
        return

    mid = len(array) // 2
    start = 0
    end = len(array) - 1
    index = partition(array, start, end)
    while index is not None and index != mid:
        if index > mid:
            end = index - 1
        else:
            start = index + 1
        index = partition(array, start, end)

    if index is None:
        return

    if not check_more_than_half(array, array[index]):
        return
    return index, array[index]


"""
解法二：根据数组特点找出时间复杂度为O(n)的算法
（不修改原数组）
"""


def find_more_than_half_num2(array):
    if not isinstance(array, list) or len(array) == 0:
        return

    result = array[0]
    count = 1
    for i in range(1, len(array)):
        if count == 0:
            result = array[i]
            count = 1
        elif result == array[i]:
            count += 1
        else:
            count -= 1

    if not check_more_than_half(array, result):
        return
    return result


if __name__ == "__main__":
    print(find_more_than_half_num1([1, 2, 3, 2, 2, 2, 5, 4, 2]))
