#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix by 90 degrees clockwise.

    Args:
        matrix (List[List[int]]): The 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in-place.

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6],
        ...     [7, 8, 9]
        ... ]
        >>> rotate_2d_matrix(matrix)
        >>> for row in matrix:
        ...     print(row)
        [7, 4, 1]
        [8, 5, 2]
        [9, 6, 3]
    """
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse rows
    for row in matrix:
        row.reverse()
