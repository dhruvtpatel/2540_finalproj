import math
import datetime


def matrix_determinant_transformed(matrix: list):
    '''
    pre: len(matrix) == 2 and all(len(row) == 2 for row in matrix) and all(isinstance(val, (int, float)) for row in matrix for val in row)
    post: (abs(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 50 == 15) == (abs(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 50 == 15)
    '''
    b_early = (abs(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 50 == 15)
    
    a, b = matrix[0]
    c, d = matrix[1]
    
    det = a * d - b * c
    scaled = abs(det) % 50
    b_final = (scaled == 15)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return scaled
