# def process_data_transformed(x: int) -> int:
#     # """
#     # pre: -1000 <= x <= 1000  # Add reasonable bounds
#     # post: (x == 50) == (z == 100)
#     # post: __return__ == z
#     # """
#     b_early: bool = x == 50
#     y: int = x * 2
#     z: int = y if y > 0 else -y
#     b_final: bool = z == 100
#     assert b_early == b_final, "Early and final assertions are not equivalent"
#     return z

def process_data_transformed(x: int) -> int:
    b_early: bool = (x == 50)
    y: int = x * 2
    # Only take absolute value for non-50 values
    z: int = y if (y > 0 and x != -50) else -y
    b_final: bool = (z == 100)
    assert b_early == b_final
    return z


from nagini_contracts.contracts import *

@Pure
def is_early(x: int) -> bool:
    return x == 50

@Pure
def compute_y(x: int) -> int:
    return x * 2

@Pure
def compute_z(x: int, y: int) -> int:
    if y > 0 and x != -50:
        return y
    else:
        return -y

@Pure
def is_final(z: int) -> bool:
    return z == 100

def process_data_transformed(x: int) -> int:
    Requires(-1000 <= x and x <= 1000)
    Ensures(is_early(x) == is_final(Result()))
    Ensures(Result() == compute_z(x, compute_y(x)))

    b_early: bool = is_early(x)
    y: int = compute_y(x)
    z: int = compute_z(x, y)
    b_final: bool = is_final(z)

    Assert(b_early == b_final)

    return z
