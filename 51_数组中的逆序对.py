def count_inverse_pair(array):
    if not isinstance(array, list) or len(array) == 0:
        return array

    copy_array = [x for x in array]
    result = count_inverse_pair_core(array, copy_array, 0, len(array) - 1)
    print(copy_array)
    return result


def count_inverse_pair_core(array, copy_array, start, end):
    if start == end:
        copy_array[start] = array[start]
        return 0

    mid = (end - start) // 2
    left_count = count_inverse_pair_core(array, copy_array, start, start + mid)
    right_count = count_inverse_pair_core(array, copy_array, start + mid + 1, end)

    count = 0
    i = start + mid
    j = end
    index = end
    while i >= start and j >= start + mid + 1:
        if array[i] > array[j]:
            copy_array[index] = array[i]
            count += j - start - mid
            i -= 1
        else:
            copy_array[index] = array[j]
            j -= 1
        index -= 1

    while i >= start:
        copy_array[index] = array[i]
        i -= 1
        index -= 1

    while j >= start + mid + 1:
        copy_array[index] = array[j]
        j -= 1
        index -= 1

    for i in range(start, end + 1):
        array[i] = copy_array[i]

    return left_count + right_count + count


if __name__ == "__main__":
    print(count_inverse_pair([7, 5, 6, 4]))
