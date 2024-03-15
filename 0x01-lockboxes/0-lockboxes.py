#!/usr/bin/python3

def canUnlockAll(boxes):
    # A function that checks if all boxes can be open
    n = len(boxes)
    visited = set()

    def dfs(box_index):
        # A function that check keys and add each key to visited 
        visited.add(box_index)
        for key in boxes[box_index]:
            # loop through each box and check if key is visited or not
            if key < n and key not in visited:
                dfs(key)

    dfs(0)
    return len(visited) == n
