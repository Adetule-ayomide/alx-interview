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

    def dfs(box_index):
        """ A function that check keys and add each key to visited"""
        visited.add(box_index)
        for key in boxes[box_index]:
            if key < n and key not in visited:
                dfs(key)

    dfs(0)
    return len(visited) == n
