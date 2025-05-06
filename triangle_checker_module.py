
def triangle_checker_transformed(a: int, b: int, c: int):
    '''
    pre: 1 <= a <= 20  # Add reasonable side length bounds
    pre: 1 <= b <= 20
    pre: 1 <= c <= 20
    post: (a + b > c and a + c > b and b + c > a) == (sorted([a, b, c])[0] + sorted([a, b, c])[1] > sorted([a, b, c])[2])
    '''
    b_early = (a + b > c and a + c > b and b + c > a)
    sides = sorted([a, b, c])
    is_triangle = sides[0] + sides[1] > sides[2]
    code = 100 if is_triangle else 0
    b_final = (code == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return code
