def replace_space(string):
    """
    O(n)
    """
    if not isinstance(string, str) or len(string) == 0:
        return None

    string = list(string)
    p1 = len(string) - 1
    for ch in string:
        if ch == " ":
            string.append(None)
            string.append(None)

    p2 = len(string) - 1
    while p1 != p2:
        if string[p1] != " ":
            string[p2] = string[p1]
            p2 -= 1
        else:
            string[p2 - 2:p2 + 1] = ["%", "2", "0"]
            p2 -= 3
        p1 -= 1
    return "".join(string)


if __name__ == "__main__":
    print(replace_space("we are friend"))
