from functools import cmp_to_key


def compare(a, b):
    assert isinstance(a, str) and isinstance(b, str)
    ab = a + b
    ba = b + a
    if ab < ba:
        return -1
    elif ab > ba:
        return 1
    else:
        return 0


def construct_min_number(array):
    assert isinstance(array, list) and len(array) > 0
    array_of_str = [str(x) for x in array]
    array_of_str = sorted(array_of_str, key=cmp_to_key(compare))
    return "".join(array_of_str)


if __name__ == "__main__":
    print(construct_min_number([3, 32, 321]))
