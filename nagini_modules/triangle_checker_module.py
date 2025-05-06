from typing import List

# def triangle_checker_transformed(a: int, b: int, c: int) -> int:
#     '''
#     pre: 1 <= a <= 20  # Add reasonable side length bounds
#     pre: 1 <= b <= 20
#     pre: 1 <= c <= 20
#     post: __return__ == code
#     post: code == (100 if is_triangle else 0)
#     '''
#     b_early: bool = (a + b > c and a + c > b and b + c > a)
    
#     # Manual sorting of three values
#     sides: List[int] = [a, b, c]
#     # Bubble sort for simplicity
#     for i in range(2):
#         for j in range(2 - i):
#             if sides[j] > sides[j + 1]:
#                 # Swap elements properly
#                 temp = sides[j]
#                 sides[j] = sides[j + 1]
#                 sides[j + 1] = temp
    
#     is_triangle: bool = sides[0] + sides[1] > sides[2]
#     code: int = 100 if is_triangle else 0
#     b_final: bool = (code == 100)
#     assert b_early == b_final, "Early and final assertions are not equivalent"
#     return code 

from nagini_contracts.contracts import *

def triangle_checker_transformed(a: int, b: int, c: int) -> int:
    Requires(1 <= a and a <= 20)
    Requires(1 <= b and b <= 20)
    Requires(1 <= c and c <= 20)
    Ensures(Result() == (100 if (a + b > c and a + c > b and b + c > a) else 0))
    
    b_early: bool = (a + b > c and a + c > b and b + c > a)
    
    # Manual sorting of three values
    sides: List[int] = [a, b, c]
    
    # Simply declare permission to the list
    Acc(list_pred(sides))
    
    # Bubble sort for simplicity
    # Note: Invariant goes BEFORE the loop body begins
    Invariant[i](Acc(list_pred(sides)))
    for i in range(2):
        # Inner loop
        Invariant[j](Acc(list_pred(sides)))
        for j in range(2 - i):
            if sides[j] > sides[j + 1]:
                # Swap elements properly
                temp = sides[j]
                sides[j] = sides[j + 1]
                sides[j + 1] = temp
    
    is_triangle: bool = sides[0] + sides[1] > sides[2]
    code: int = 100 if is_triangle else 0
    b_final: bool = (code == 100)
    Assert(b_early == b_final)
    return code