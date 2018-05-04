def get_max_value1(matrix):
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        return

    num_row = len(matrix)
    num_col = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) != num_col:
            return

    max_value_matrix = [[0] * num_col for _ in range(num_row)]
    for i in range(num_row):
        for j in range(num_col):
            up = 0
            left = 0
            if i > 0:
                up = max_value_matrix[i - 1][j]

            if j > 0:
                left = max_value_matrix[i][j - 1]
            max_value_matrix[i][j] = matrix[i][j] +  max(up, left)
    return max_value_matrix[-1][-1]


def get_max_value2(matrix):
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        return

    num_row = len(matrix)
    num_col = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) != num_col:
            return

    max_values = [0] * num_col
    for i in range(num_row):
        for j in range(num_col):
            up = 0
            left = 0
            if i > 0:
                up = max_values[j]

            if j > 0:
                left = max_values[j - 1]
            max_values[j] = matrix[i][j] + max(up, left)
    return max_values[-1]


if __name__ == "__main__":
    m = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    print(get_max_value2(m))
