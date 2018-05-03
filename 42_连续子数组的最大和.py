def find_the_greatest_sum_of_sub_array(array):
    if not isinstance(array, list) or len(array) == 0:
        return

    result = array[0]
    sum = 0

    for x in array:
        if sum < 0:
            sum = x
        else:
            sum += x

        if sum > result:
            result = sum
    return result


if __name__ == "__main__":
    print(find_the_greatest_sum_of_sub_array([1, -2, 3, 10, -4, 7, 2, -5]))
