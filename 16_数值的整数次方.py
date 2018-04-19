def power(base, exponent):
    if base == 0 and exponent == 0:
        return None

    unsigned_exponent = exponent if exponent >= 0 else abs(exponent)
    result = unsigned_power(base, unsigned_exponent)
    if exponent < 0:
        return 1.0 / result
    return result


def unsigned_power(base, unsigned_exponent):
    """
    二分法计算a的b次方
    """
    if unsigned_exponent == 0:
        return 1

    if unsigned_exponent == 1:
        return base

    result = unsigned_power(base, unsigned_exponent >> 1)
    result *= result
    if unsigned_exponent & 1 == 1:
        result *= base
    return result


if __name__ == "__main__":
    print(power(2, -4))

