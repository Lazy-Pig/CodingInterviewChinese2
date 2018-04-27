def verify_sequence_of_BST(sequence):
    if not isinstance(sequence, list) or len(sequence) == 0:
        return False

    root = sequence[-1]
    for index, element in enumerate(sequence):
        i = index
        if element > root:
            break

    for element in sequence[i:]:
        if element < root:
            return False

    left = True
    if i > 0:
        left = verify_sequence_of_BST(sequence[:i])

    right = True
    if i < len(sequence) - 1:
        right = verify_sequence_of_BST(sequence[i:-1])

    return left and right


if __name__ == "__main__":
    print(verify_sequence_of_BST([5, 7, 6, 9, 11, 10, 8]))
    print(verify_sequence_of_BST([7, 4, 6, 5]))
