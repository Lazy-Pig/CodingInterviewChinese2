def fibonacci(n):
    f_x_minus_2 = 0
    f_x_minus_1 = 1
    if n == 0:
        return f_x_minus_2
    if n == 1:
        return f_x_minus_1

    x = 2
    while x <= n:
        f_x = f_x_minus_1 + f_x_minus_2
        f_x_minus_2 = f_x_minus_1
        f_x_minus_1 = f_x
        x += 1
    return f_x


if __name__ == "__main__":
    print(fibonacci(2))
