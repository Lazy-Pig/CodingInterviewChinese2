def is_continuous(array):
    if not isinstance(array, list) or len(array) != 5:
        return False

    preprocessing(array)
    sorted_array = sorted(array)
    num_of_zero = 0
    for x in sorted_array:
        if x != 0:
            break
        num_of_zero += 1

    small = num_of_zero
    big = small + 1
    num_of_gap = 0
    while big < len(array):
        if sorted_array[big] == sorted_array[small]:
            return False

        num_of_gap += sorted_array[big] - sorted_array[small] - 1
        small = big
        big += 1
    return num_of_gap <= num_of_zero


def preprocessing(array):
    char_2_num = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    for i, x in enumerate(array):
        if x in char_2_num:
            array[i] = char_2_num[x]
        elif not isinstance(x, int):
            array[i] = 0


if __name__ == "__main__":
    print(is_continuous([2, 4, 5, 'w', 'w']))
