#!/usr/bin/python3
""" A script to determinr pascal's triangle for any number"""


def pascal_triangle(n):
    """
    return a list of lists of integers represening the pascal's triangle of n
    """
    triangle =[]

    # return (triangle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
    # print(triangle)
    return triangle
