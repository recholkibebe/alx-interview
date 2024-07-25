#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers 
    representing the Pascal’s triangle of n:
    """
    if n <= 0:
        return []

    pascal = []

    for i in range(n):
        row = [1] * (i + 1)  # Create a row with all elements set to 1
        for j in range(1, i):
            row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal.append(row)

    return pascal

# Example usage:
if __name__ == "__main__":
    n = 5
    for row in pascal_triangle(n):
        print(row)

