#!/usr/bin/python3

""" You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
    Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """ A function that checks if all boxes can be open """
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        box_index = stack.pop()
        visited.add(box_index)
        for key in boxes[box_index]:
            if key < n and key not in visited:
                stack.append(key)

    return len(visited) == n
