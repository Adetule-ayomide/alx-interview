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
    to_visit = deque([0])

    while to_visit:
        box_index = to_visit.popleft()
        visited.add(box_index)
        for key in boxes[box_index]:
            if key < n and key not in visited:
                to_visit.append(key)

    return len(visited) == n
