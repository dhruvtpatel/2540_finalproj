import math
import datetime


def fibonacci_counter_transformed(n: int):
    '''
    pre: 0 <= n <= 20 # Increased range for n
    post: (n == 17) == (__return__ == 89)
    '''
    b_early = (n == 17)
    
    a, b = 0, 1
    fib_sum = 0
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    mod_sum = fib_sum % 100
    func_return_value = mod_sum
    b_final = (func_return_value == 89)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return func_return_value
