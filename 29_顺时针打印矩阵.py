def print_matrix_clock_wisely(matrix):
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        return

    n_row = len(matrix)
    n_col = len(matrix[0])
    for row in matrix:
        if len(row) != n_col:
            return

    start = 0
    while n_row > 2 * start and n_col > 2 * start:
        print_matrix_in_circle(matrix, n_row, n_col, start)
        start += 1


def print_matrix_in_circle(matrix, n_row, n_col, start):
    end_y = n_row - 1 - start
    end_x = n_col - 1 - start

    # 从头到尾打印一行
    for i in range(start, end_x + 1):
        print(matrix[start][i], end=' ')

    # 从上到下打印一列
    if start < end_y:
        for i in range(start + 1, end_y + 1):
            print(matrix[i][end_x], end=' ')

    # 从尾到头打印一行
    if start < end_y and start < end_x:
        for i in range(end_x - 1, start - 1, -1):
            print(matrix[end_y][i], end=' ')

    # 从下到上打印一列
    if start < end_x and start < end_y - 1:
        for i in range(end_y - 1, start, -1):
            print(matrix[i][start], end=' ')


if __name__ == "__main__":
    # m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m = [[1, 2], [3, 4], [5, 6]]
    print_matrix_clock_wisely(m)
