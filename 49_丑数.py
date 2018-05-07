def get_ugly_number(index):
    if not isinstance(index, int) or index <= 0:
        return 0

    ugly_numbers = [0] * index
    ugly_numbers[0] = 1
    index_multiply2 = 0
    index_multiply3 = 0
    index_multiply5 = 0

    next_index = 1
    while next_index < index:
        ugly_numbers[next_index] = min(ugly_numbers[index_multiply2] * 2,
                                       ugly_numbers[index_multiply3] * 3,
                                       ugly_numbers[index_multiply5] * 5)

        while ugly_numbers[index_multiply2] * 2 <= ugly_numbers[next_index]:
            index_multiply2 += 1

        while ugly_numbers[index_multiply3] * 3 <= ugly_numbers[next_index]:
            index_multiply3 += 1

        while ugly_numbers[index_multiply5] * 5 <= ugly_numbers[next_index]:
            index_multiply5 += 1

        next_index += 1
    return ugly_numbers[next_index - 1]


if __name__ == "__main__":
    print(get_ugly_number(1500))
