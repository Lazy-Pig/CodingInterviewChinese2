def count_of_integers(digits):
    if digits == 1:
        return 10

    return 9 * 10 ** (digits - 1)


def get_begin(digits):
    if digits == 1:
        return 0
    return 10 ** (digits - 1)


def real_digit_at_index(index, digits):
    if index == 0 and digits == 1:
        return 0

    index_of_number = index // digits
    index_in_number = index - index_of_number * digits
    number = get_begin(digits) + index_of_number
    return str(number)[index_in_number]


def digit_at_index(index):
    assert isinstance(index, int) and index >= 0

    digits = 1
    while True:
        numbers = digits * count_of_integers(digits)
        if index < numbers:
            return real_digit_at_index(index, digits)
        index -= numbers
        digits += 1


if __name__ == "__main__":
    print(digit_at_index(1001))
