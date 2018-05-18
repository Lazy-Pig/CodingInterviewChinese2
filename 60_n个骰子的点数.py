"""
方法一：递归， 效率低
"""


def print_probability1(num):
    num_probability = 6 * num - num + 1
    probabilitys = [0] * num_probability
    probability(num, probabilitys)

    total = 6 ** num
    for s in range(num, num * 6 + 1):
        print(s, probabilitys[s - num] / total)


def probability(number, probabilitys):
    for i in range(1, 7):
        recurrently_probability(number, number, i, probabilitys)


def recurrently_probability(origin_num, current_num, sum, probabilitys):
    if current_num == 1:
        probabilitys[sum - origin_num] += 1
    else:
        for i in range(1, 7):
            recurrently_probability(origin_num, current_num - 1, sum + i, probabilitys)


"""
方法二
"""


def print_probability2(num):
    if num < 1:
        return

    num_probability = num * 6 + 1
    probabilitys1 = [0] * num_probability
    probabilitys2 = [0] * num_probability

    for i in range(1, 7):
        probabilitys1[i] = 1

    for k in range(2, num + 1):
        currrent_probabilitys = probabilitys1 if k % 2 == 1 else probabilitys2
        last_probabilitys = probabilitys2 if k % 2 == 1 else probabilitys1

        for i in range(1, k):
            currrent_probabilitys[i] = 0

        for i in range(k, k * 6 + 1):
            currrent_probabilitys[i] = 0

            for j in range(1, 7):
                if j >= i:
                    break
                currrent_probabilitys[i] += last_probabilitys[i - j]

    result_probability = probabilitys1 if num % 2 == 1 else probabilitys2
    total = 6 ** num
    for s in range(num, 6 * num + 1):
        print(s, result_probability[s] / total)


if __name__ == "__main__":
    print_probability1(3)
    print("============")
    print_probability2(3)

