"""
题目一： 数字在排序数组中出现的次数
"""


def get_first_k(array, start, end, k):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] > k:
        return get_first_k(array, start, mid - 1, k)

    if array[mid] < k:
        return get_first_k(array, mid + 1, end, k)

    if array[mid] == k:
        if mid == 0 or array[mid - 1] != k:
            return mid

        return get_first_k(array, start, mid - 1, k)
    return None


def get_last_k(array, start, end, k):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] > k:
        return get_last_k(array, start, mid - 1, k)

    if array[mid] < k:
        return get_last_k(array, mid + 1, end, k)

    if array[mid] == k:
        if mid == len(array) - 1 or array[mid + 1] != k:
            return mid
        return get_last_k(array, mid + 1, end, k)
    return None


def count_number_of_k(array, k):
    if not isinstance(array, list) or len(array) == 0:
        return None

    for i in range(len(array) - 1, 0, -1):
        if array[i] < array[i - 1]:
            return None

    index_first_k = get_first_k(array, 0, len(array) - 1, k)
    index_last_k = get_last_k(array, 0, len(array) - 1, k)

    if index_first_k is None or index_last_k is None:
        return None

    return index_last_k - index_first_k + 1


"""
题目二： 0～n-1中缺失的数字
"""


def find_missing_number(array):
    if not isinstance(array, list) or len(array) == 0:
        return None

    length = len(array)
    if array[length - 1] > length or array[length - 1] < 0:
        return None

    for i in range(length - 1, 0, -1):
        if array[i] <= array[i - 1]:
            return None

    start = 0
    end = length - 1
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == mid:
            start = mid + 1
            continue

        if array[mid] != mid:
            if mid == 0 or array[mid - 1] == mid - 1:
                return mid
            end = mid - 1

    if start == length:
        return start
    return None


"""
题目三： 数组中数值和下标相等的元素
"""


def find_number_same_as_index(array):
    if not isinstance(array, list) or len(array) == 0 or len(array) != len(set(array)):
        return None

    for i in range(len(array) - 1, 0, -1):
        if array[i] < array[i - 1]:
            return None

    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        mid_value = array[mid] if array[mid] > 0 else array[mid] + len(array)
        if mid_value == mid:
            return mid

        if mid_value > mid:
            end = mid - 1

        if mid_value < mid:
            start = mid + 1
    return None


if __name__ == "__main__":
    # 题目一
    array = [1, 2, 3, 3, 3, 3, 4, 5]
    print(count_number_of_k(array, 3))

    # 题目二
    array = [0, 1, 2, 3, 4, 5, 6]
    print(find_missing_number(array))

    # 题目三
    array = [-3, -1, 1, 3, 5]
    print(find_number_same_as_index(array))
