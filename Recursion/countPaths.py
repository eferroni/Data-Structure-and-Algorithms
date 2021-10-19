def countPaths(arr, row, col):
    # Valid Square?
    try:
        if arr[row][col] == 0:
            return 0
    except IndexError:
        return 0
    # End?
    if row == len(arr) - 1 and col == len(arr[row]) - 1:
        return 1
    # Recursion
    return countPaths(arr, row + 1, col) + countPaths(arr, row, col + 1)


def countPaths2(arr, row, col, path=[[0] * 8] * 8):
    # Valid Square?
    try:
        if arr[row][col] == 0:
            return 0
    except IndexError:
        return 0
    # End?
    if row == len(arr) - 1 and col == len(arr[row]) - 1:
        return 1
    # Recursion
    if path[row][col] == 0:
        path[row][col] = countPaths(arr, row + 1, col) + countPaths(arr, row, col + 1)
    return path


my_arr = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]
print(countPaths(my_arr, 0, 0))
