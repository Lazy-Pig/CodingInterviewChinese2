def translation_count(num):
    if not isinstance(num, int) or num < 0:
        return

    str_num = str(num)
    length = len(str_num)
    counts = [0] * length

    for i in range(length - 1, -1, -1):
        if i == length - 1:
            counts[i] = 1
            continue

        count = counts[i + 1]
        value = (ord(str_num[i]) - ord('0')) * 10 + (ord(str_num[i + 1]) - ord('0'))
        if i == length - 2:
            count += 1 if 10 <= value <= 25 else 0
        else:
            count += counts[i + 2] if 10 <= value <= 25 else 0
        counts[i] = count
    return counts[0]


if __name__ == "__main__":
    print(translation_count(12258))
