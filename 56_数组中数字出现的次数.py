"""
题目一： 数组中之出现一次的两个数字
"""


def find_nums_appear_once(array):
    if not isinstance(array, list) or len(array) == 0:
        return

    temp = 0
    for x in array:
        temp ^= x

    index_of_1 = find_first_bit_is_1(temp)
    temp = 1 << index_of_1

    res1 = 0
    res2 = 0
    for x in array:
        if x & temp:
            res1 ^= x
        else:
            res2 ^= x
    return res1, res2


def find_first_bit_is_1(num):
    if not isinstance(num, int):
        return

    index_of_bit = 0
    while num != 0 and num & 1 == 0:
        num = num >> 1
        index_of_bit += 1
    return index_of_bit


"""
题目二： 数组中唯一只出现一次的数字
"""


def find_num_appear_once(array):
    if not isinstance(array, list) or len(array) == 0:
        return

    max_length = max([len(bin(x)) for x in array]) - 2
    bits_count = [0] * max_length
    for x in array:
        bit_mask = 1
        for bit_index in range(max_length - 1, -1, -1):
            if x & bit_mask != 0:
                bits_count[bit_index] += 1
            bit_mask = bit_mask << 1

    result = 0
    for count in bits_count:
        result = result << 1
        result += count % 3
    return result


if __name__ == "__main__":
    print(find_nums_appear_once([-8, -4, 3, 6, 3, -8, 5, 5]))
    print(find_num_appear_once([2, 18, 3, 7, 3, 3, 2, 7, 2, 7]))
