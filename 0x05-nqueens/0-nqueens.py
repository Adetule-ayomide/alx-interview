#!/usr/bin/python3

import sys

"""
    The N queens puzzle is the challenge of placing N
    non-attacking queens on an N×N chessboard.
    Write a program that solves the N queens problem.
"""


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append([(i, col) for i, col in enumerate(board[row - 1])])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0


def print_solution(solution):
    for row, col in solution:
        print("[{}, {}]".format(row, col), end=" ")
    print()


def solve_n_queens(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    for solution in solutions:
        print_solution(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_n_queens(sys.argv[1])
