def longest_substring_without_duplication(string):
    if not isinstance(string, str) or len(string) == 0:
        return

    max_length = 0
    current_length = 0
    position = [-1] * 26

    for i, ch in enumerate(string):
        if ord(ch) < ord("a") or ord(ch) > ord("z"):
            return

        index_of_position = ord(ch) - ord("a")
        if position[index_of_position] == -1 or (i - position[index_of_position]) > max_length:
            current_length += 1
        else:
            current_length = i - position[index_of_position]

        if current_length > max_length:
            max_length = current_length

        position[index_of_position] = i
    return max_length


if __name__ == "__main__":
    print(longest_substring_without_duplication("arabcacfr"))
