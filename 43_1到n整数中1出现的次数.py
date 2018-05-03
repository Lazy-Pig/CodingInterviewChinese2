def given_digits_get_1_num(n):
    """
    例如，n为3,返回1～999中有多少个1

    @param n: n位数
    """
    assert isinstance(n, int)
    if n <= 0:
        return 0

    if n == 1:
        return 1

    f_n_minus_1 = 1
    for i in range(2, n + 1):
        f_n = 10 * f_n_minus_1 + 10 ** (i - 1)
        f_n_minus_1 = f_n
    return f_n


def get_digits(number):
    result = 0
    while number:
        result += 1
        number = number // 10
    return result


def given_number_get_1_num(number):
    assert isinstance(number, int)
    if number <= 0:
        return 0

    digits = get_digits(number)

    if digits == 1:
        return 1

    # 例如， 23456
    # hight = 2
    # low = 3456
    hight = number // (10 ** (digits - 1))
    low = number - hight * 10 ** (digits - 1)

    # 1~9999中1的个数
    low_num_of_1 = given_digits_get_1_num(digits - 1)

    if hight == 1:
        return low_num_of_1 + low + 1

    return low_num_of_1 * hight + 10 ** (digits - 1) + given_number_get_1_num(low)


def test_n(num):
    # 常规方法用来比较
    ret = 0
    for n in range(1, num+1):
        for s in str(n):
            if s == '1':
                ret += 1
    return ret


if __name__ == "__main__":
    print(given_number_get_1_num(9923446))
    print(test_n(9923446))
