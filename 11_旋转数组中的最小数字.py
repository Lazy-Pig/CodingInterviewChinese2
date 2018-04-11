def find_in_order(numbers):
    min_index = 0
    for i in range(len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
    return min_index, numbers[min_index]


def find_min_in_rotated_arr(numbers):
    p1 = 0
    p2 = len(numbers) - 1
    while numbers[p1] >= numbers[p2]:
        if p2 - p1 == 1:
            return p2, numbers[p2]

        mid = (p1 + p2) // 2
        # 两端和中间三个数相等时 只能顺序查找
        if numbers[mid] == numbers[p1] and numbers == numbers[p2]:
            return find_in_order(numbers[p1:p2 + 1])

        if numbers[mid] >= numbers[p1]:
            p1 = mid
        else:
            p2 = mid
    return p1, numbers[p1]


if __name__ == "__main__":
    print(find_in_order([3, 4, 5, 1, 2]))
    print(find_in_order([1, 1, 1, 1, 1]))
