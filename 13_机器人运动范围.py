def moving_count(matrix, k):
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    for r in matrix:
        if len(r) != cols:
            return False

    visited = [[False] * cols for _ in range(rows)]
    count = count_recursively(matrix, k, (0, 0), visited)
    return count


def count_recursively(matrix, k, matrix_indices, visited):
    count = 0
    m_i, m_j = matrix_indices
    if check(matrix, k, matrix_indices, visited):
        count = count + count_recursively(matrix, k, (m_i + 1, m_j), visited) + \
            count_recursively(matrix, k, (m_i - 1, m_j), visited) + \
            count_recursively(matrix, k, (m_i, m_j + 1), visited) + \
            count_recursively(matrix, k, (m_i, m_j - 1), visited)
    return count


def check(matrix, k , matrix_indices, visited):
    m_i, m_j = matrix_indices
    if not (0 <= m_i < len(matrix)) or not (0 <= m_j < len(matrix[0])) or \
            (sum_digit(m_i) + sum_digit(m_j) > k) or \
            visited[m_i][m_j]:
        return False
    return True


def sum_digit(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum