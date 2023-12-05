#!/usr/bin/python3
'''
Make a Pascal Tiangle
'''


def pascal_triangle(n):
    """"
    Pascal triangle of height n:

    Args:
    n (int): The Triangle height
    Return:
    list of lists of integers representing the Pascal triangle
    """
    if n <= 0:
        return []
    pascal_t = [[1]]
    idx = 0
    while idx < n - 1:
        row = []
        row.append(1)
        for jdx in range(idx):
            prev_row = pascal_t[idx]
            row.append(prev_row[jdx] + prev_row[jdx + 1])
        row.append(1)
        idx += 1
        pascal_t.append(row)

    return (pascal_t)
