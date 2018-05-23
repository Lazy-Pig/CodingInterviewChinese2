def max_diff(array):
    if not isinstance(array, list) or len(array) < 2:
        return

    for x in array:
        if not isinstance(x, int) or x < 0:
            return

    min = array[0]
    result = array[1] - min

    for i in range(2, len(array)):
        if array[i - 1] < min:
            min = array[i - 1]
        if array[i] - min > result:
            result = array[i] - min
    return result


if __name__ == "__main__":
    print(max_diff([9, 11, 8, 5, 7, 12, 16, 14]))
