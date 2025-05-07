from nagini_contracts.contracts import *

@Pure
def min_value(a: int, b: int) -> int:
    """Return the minimum of two integers"""
    if a <= b:
        return a
    return b

@Pure
def max_value(a: int, b: int) -> int:
    """Return the maximum of two integers"""
    if a >= b:
        return a
    return b

def calculate_overlap_width(x1: int, w1: int, x2: int, w2: int) -> int:
    """Calculate the width of the overlap between two rectangles"""
    Requires(True)
    
    right1 = x1 + w1
    right2 = x2 + w2
    
    left = max_value(x1, x2)
    right = min_value(right1, right2)
    
    if right > left:
        return right - left
    else:
        return 0

def calculate_overlap_height(y1: int, h1: int, y2: int, h2: int) -> int:
    """Calculate the height of the overlap between two rectangles"""
    Requires(True)
    
    bottom1 = y1 + h1
    bottom2 = y2 + h2
    
    top = max_value(y1, y2)
    bottom = min_value(bottom1, bottom2)
    
    if bottom > top:
        return bottom - top
    else:
        return 0

def rectangle_overlap_area_transformed(x1: int, y1: int, w1: int, h1: int, x2: int, y2: int, w2: int, h2: int) -> int:
    """Calculate the area of overlap between two rectangles"""
    Requires(True)
    
    # Calculate the width and height of the overlap
    overlap_width = calculate_overlap_width(x1, w1, x2, w2)
    overlap_height = calculate_overlap_height(y1, h1, y2, h2)
    
    # Calculate the area
    area = overlap_width * overlap_height
    
    return area
