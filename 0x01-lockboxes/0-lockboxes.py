def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()

    def dfs(box_index):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key < n and key not in visited:
                dfs(key)

    dfs(0)
    return len(visited) == n

if __name__ == '__main__':
    canUnlockAll(boxes);
