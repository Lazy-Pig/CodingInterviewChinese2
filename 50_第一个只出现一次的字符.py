"""
题目一： 字符串只出现一次的字符
"""


def first_not_repeating_char(string):
    if not isinstance(string, str) or len(string) == 0:
        return

    char_2_count = {}
    for ch in string:
        if ch not in char_2_count:
            char_2_count[ch] = 1
        else:
            char_2_count[ch] += 1

    for ch in string:
        if char_2_count[ch] == 1:
            return ch
    return None


"""
题目二： 字符留中第一个之出现一次的字符
"""


def first_not_repeating_char2():
    char_2_index = {}
    index = 0
    while True:
        ch = input()
        if ch == '':
            break

        if ch not in char_2_index:
            char_2_index[ch] = index
        else:
            char_2_index[ch] = -1
        index += 1

    result = index
    for ch, index in char_2_index.items():
        if index != -1 and index < result:
            result = index
    return result


if __name__ == "__main__":
    print(first_not_repeating_char("abaccdeff"))
    print(first_not_repeating_char2())
