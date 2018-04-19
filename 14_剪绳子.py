def max_product_after_cuting1(length):
    """
    动态规划解法
    时间 O(n^2)，空间O(n)
    """
    if not isinstance(length, int):
        return

    if length < 2:
        return 0

    if length == 2:
        return 1

    if length == 3:
        return 2

    products = [0 for _ in range(length + 1)]
    # 作废
    products[0] = 0
    # 切割后两部分绳子中，长度为1的那部分最大乘积是1
    products[1] = 1
    # 切割后两部分绳子中，长度为2的那部分，不再切割乘积是2, 因为再切割后会变成1×1=1
    products[2] = 2
    # 切割后两部分绳子中，长度为3的那部分，不再切割乘积是3, 因为再切割后会变成1×2=2
    products[3] = 3

    for i in range(4, length + 1):
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i - j]
            if product > products[i]:
                products[i] = product
    return products[length]


def max_product_after_cuting2(length):
    """
    贪婪法
    时间 O(1)，空间O(1)
    """
    if not isinstance(length, int):
        return

    if length < 2:
        return 0

    if length == 2:
        return 1

    if length == 3:
        return 2

    times_of_3 = length // 3
    if (length - 3 * times_of_3) == 1:
        times_of_3 -= 1

    times_of_2 = (length - 3 * times_of_3) / 2
    return int((3 ** times_of_3) * (2 ** times_of_2))


if __name__ == "__main__":
    print(max_product_after_cuting1(3))
    print(max_product_after_cuting2(3))
