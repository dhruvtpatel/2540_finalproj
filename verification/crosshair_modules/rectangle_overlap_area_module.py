import math
import datetime


def rectangle_overlap_area_transformed(x1: int, y1: int, w1: int, h1: int, x2: int, y2: int, w2: int, h2: int):
    '''
    pre: all(-100 <= val <= 100 for val in [x1, y1, x2, y2])
    pre: all(0 <= val <= 100 for val in [w1, h1, w2, h2]) # Widths/heights non-negative
    post: (max(0, min(x1 + w1, x2 + w2) - max(x1, x2)) * max(0, min(y1 + h1, y2 + h2) - max(y1, y2)) == 16) == (max(0, min(x1 + w1, x2 + w2) - max(x1, x2)) * max(0, min(y1 + h1, y2 + h2) - max(y1, y2)) == 16)
    '''
    b_early = (max(0, min(x1 + w1, x2 + w2) - max(x1, x2)) * 
               max(0, min(y1 + h1, y2 + h2) - max(y1, y2)) == 16)
    overlap_width = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    overlap_height = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    area = overlap_width * overlap_height
    b_final = (area == 16)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return area
