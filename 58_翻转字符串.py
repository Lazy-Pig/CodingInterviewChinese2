"""
题目一： 翻转单词顺序
"""


def reverse_sentence(string):
    if not isinstance(string, str):
        return

    list_of_char = list(string)
    p_begin = 0
    p_end = len(list_of_char) - 1
    reverse(list_of_char, p_begin, p_end)

    p_begin = 0
    p_end = 0
    while p_begin < len(list_of_char) - 1:
        if list_of_char[p_begin] == " ":
            p_begin += 1
            p_end += 1
        elif list_of_char[p_end] == " " or p_end == len(list_of_char) - 1:
            p_end -= 1
            reverse(list_of_char, p_begin, p_end)
            p_end += 1
            p_begin = p_end
        else:
            p_end += 1
    return "".join(list_of_char)


def reverse(array, begin, end):
    while begin < end:
        array[begin], array[end] = array[end], array[begin]
        begin += 1
        end -= 1


"""
题目二： 左旋转字符串
"""


def rotate_string(string, n):
    if not isinstance(string, str) or len(string) == 0 or n < 1 or n >= len(string):
        return string

    list_of_char = list(string)

    reverse(list_of_char, 0, n - 1)
    reverse(list_of_char, n, len(string) - 1)
    reverse(list_of_char, 0, len(string) - 1)
    return "".join(list_of_char)


if __name__ == "__main__":
    print(reverse_sentence("I am a student."))
    print(rotate_string("abcdefg", 2))
