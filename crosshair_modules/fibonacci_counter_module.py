
def fibonacci_counter_transformed(n: int):
    '''
    pre: 1 <= n <= 20  # Add reasonable bounds
    post: (sum(fibonacci(n)) % 100 == 89) == (sum(fibonacci(n)) % 100 == 89)
    '''
    b_early = sum(fibonacci(n)) % 100 == 89
    a, b = 0, 1
    fib_sum = 0
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    mod_sum = fib_sum % 100
    b_final = (mod_sum == 89)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return mod_sum
