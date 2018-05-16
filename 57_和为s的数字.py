"""
题目一： 和为s的两个数字
"""


def find_nums_with_sum(array, sum):
    if not isinstance(array, list) or len(array) == 0 or not isinstance(sum, int):
        return

    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == sum:
            return True, array[left], array[right]

        if current_sum < sum:
            left += 1

        if current_sum > sum:
            right -= 1

    return False, None, None


"""
题目二： 和为s的连续正数序列
"""


def find_continuous_sequence(target):
    if not isinstance(target, int) or target <= 0:
        return

    left = 1
    right = 2
    middle = (target + 1) // 2

    while left < middle:
        sequence = [x for x in range(left, right + 1)]
        current_sum = sum(sequence)
        if current_sum == target:
            print(sequence)
            right += 1

        if current_sum > target:
            left += 1

        if current_sum < target:
            right += 1


if __name__ == "__main__":
    print(find_nums_with_sum([1, 2, 4, 7, 11, 15], 20))
    find_continuous_sequence(15)
