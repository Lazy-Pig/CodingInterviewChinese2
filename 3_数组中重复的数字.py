"""
以下均为找出数组中任意一个重复的数字
"""


def duplicate1(numbers):
    """
    题目一 找出数组中重复的数字
    原地修改数组
    时间O(n), 空间O(1)
    """
    if not isinstance(numbers, list) or len(numbers) <= 0:
        return False, None

    for num in numbers:
        if not isinstance(num, int) or num >= len(numbers) or num < 0:
            return False, None

    for index in range(len(numbers)):
        while numbers[index] != index:
            if numbers[numbers[index]] == numbers[index]:
                # 找到重复数字
                return True, numbers[index]
            numbers[numbers[index]], numbers[index] = numbers[index], numbers[numbers[index]]

    return False, None


def duplicate2(numbers):
    """
    题目二 不修改数组找出重复的数字
    时间O(n), 空间O(n)
    """
    if not isinstance(numbers, list) or len(numbers) <= 0:
        return False, None

    copy_numbers = [None] * len(numbers)
    for num in numbers:
        if not isinstance(num, int) or num < 1 or num > len(numbers) - 1:
            return False, None

        if copy_numbers[num] == num:
            return True, num
        copy_numbers[num] = num
    return False, None


def duplicate3(numbers):
    """
    题目二 不修改数组找出重复的数字
    时间O(n * log n), 空间O(1)
    """
    if not isinstance(numbers, list) or len(numbers) <= 0:
        return False, None

    for num in numbers:
        if not isinstance(num, int) or num < 1 or num > len(numbers) - 1:
            return False, None

    low = 1
    hight = len(numbers) - 1
    while low != hight:
        mid = (low + hight) // 2
        count_left = count_in_range(numbers, low, mid)
        if count_left > mid - low + 1:
            hight = mid
        else:
            low = mid + 1
    return True, low


def count_in_range(numbers, low, hight):
    """
    O(n)
    """
    count = 0
    for num in numbers:
        if low <= num <= hight:
            count += 1
    return count


if __name__ == "__main__":
    print(duplicate1([2, 3, 1, 2, 5, 3, 0]))
    print(duplicate1([2, 1, 0]))
    print(duplicate3([2, 3, 1, 2, 5, 3]))
    print(duplicate3([2, 1, 1]))

