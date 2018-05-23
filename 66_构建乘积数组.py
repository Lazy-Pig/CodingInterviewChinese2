def multiply(array):
    if not isinstance(array, list) or len(array) == 0:
        return

    result = [1]
    for i in range(1, len(array)):
        result.append(array[i - 1] * result[i - 1])

    temp = 1
    for i in range(len(array) - 2, -1, -1):
        temp *= array[i + 1]
        result[i] *= temp
    return result


if __name__ == "__main__":
    print(multiply([1, 2, 3, 4]))
