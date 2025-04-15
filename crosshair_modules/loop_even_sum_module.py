
def loop_even_sum_transformed(start: int, end: int):
    '''
    pre: 0 <= start <= 100  # Add reasonable bounds
    pre: 0 <= end <= 100
    post: (sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110) == (sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110)
    '''
    b_early = sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    final = total // 2
    b_final = (final == 110)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
